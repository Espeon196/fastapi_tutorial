from fastapi import FastAPI
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
)

app = FastAPI()


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/text", response_class=PlainTextResponse)
async def read_text():
    return "Hello World"


@app.get("/redirect", response_class=RedirectResponse)
async def redirect():
    return RedirectResponse("https://fastapi.tiangolo.com")


@app.get("/file/", response_class=FileResponse)
async def read_file():
    file_path = "nanjamo.jpg"
    return FileResponse(file_path)
