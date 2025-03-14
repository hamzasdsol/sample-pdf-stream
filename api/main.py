from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.responses import StreamingResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range", "Accept-Ranges", "Content-Length"],
)

PDF_PATH = "pdf/20-test.pdf"
# PDF_PATH = "pdf/test_linearized.pdf"

@app.get("/")
def read_root():
    return {"message": "PDF API is running!"}

def get_file_size(file_path: str) -> int:
    """Returns the size of the file in bytes."""
    return os.path.getsize(file_path)

def file_iterator(file_path: str, start: int, end: int, chunk_size=1 * 1024 * 1024):
    """Generator function to stream the file in multiple chunks."""
    with open(file_path, "rb") as f:
        f.seek(start)
        remaining = end - start + 1
        while remaining > 0:
            chunk = f.read(min(chunk_size, remaining))
            if not chunk:
                break
            yield chunk
            remaining -= len(chunk)

@app.get("/pdf")
async def get_pdf(request: Request, range: str = Header(None)):
    """Handles either full-file or partial-file responses, depending on Range header."""
    if not os.path.exists(PDF_PATH):
        raise HTTPException(status_code=404, detail="PDF not found")

    file_size = get_file_size(PDF_PATH)

    # ----------------------------
    # 1) No Range Header → Full File
    # ----------------------------
    if not range:
        # Return the entire file using FileResponse, plus 'Accept-Ranges: bytes'
        return FileResponse(
            PDF_PATH,
            headers={"Accept-Ranges": "bytes"},
            media_type="application/pdf"
        )

    # ----------------------------
    # 2) Range Header → Partial Content
    # ----------------------------
    try:
        # Parse the "bytes=start-end" format
        range_value = range.replace("bytes=", "").strip()
        start_str, end_str = range_value.split("-")

        start = int(start_str)
        # If 'end' is empty, default to a chunk of CHUNK_SIZE from start
        if end_str:
            end = int(end_str)
        else:
            end = start + (1 * 1024 * 1024)  # 1MB chunk if end not specified

        # Validate bounds
        end = min(end, file_size - 1)
        start = min(start, end)

    except ValueError:
        # Invalid Range format
        return Response(status_code=416)

    content_length = end - start + 1

    headers = {
        "Content-Range": f"bytes {start}-{end}/{file_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": str(content_length),
        "Content-Type": "application/pdf",
    }

    return StreamingResponse(
        file_iterator(PDF_PATH, start, end),
        headers=headers,
        status_code=206
    )
