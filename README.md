# PDF-STREAM

## 🚀 Getting Started

### 1. Backend (API) - Python FastAPI

#### Prerequisites

- Python 3.9+
- Virtual environment tool (`venv`)

#### Installation

1. Navigate to the `api/` directory:
   ```sh
   cd api
   ```
2. Create and activate a virtual environment:
   - macOS/Linux:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the API server:
   ```sh
   uvicorn main:app --reload
   ```
5. The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 2. Frontend (UI) - React with TypeScript

#### Prerequisites

- Node.js 18+
- npm or Yarn

#### Installation

1. Navigate to the `ui/` directory:
   ```sh
   cd ui
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
   OR, if using Yarn:
   ```sh
   yarn install
   ```
3. Run the frontend:
   ```sh
   npm run dev
   ```
   OR with Yarn:
   ```sh
   yarn dev
   ```
4. The UI will be available at: [http://localhost:3000](http://localhost:3000)
