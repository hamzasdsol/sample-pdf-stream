import { Root, Pages, Page, CanvasLayer, TextLayer } from '@unriddle-ai/lector'

export function PDFViewer() {
  return (
    <Root
      source={{
        url: 'http://127.0.0.1:8000/pdf',
        rangeChunkSize: 10 * 1024 * 1024,
        disableRange: false,
        disableStream: false,
      }}
      loader={<div className='p-4'>Loading...</div>}
    >
      <Pages>
        <Page>
          <CanvasLayer />
          <TextLayer />
        </Page>
      </Pages>
    </Root>
  )
}
