from typing import Optional
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_file(file: Optional[bytes] = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    return {"file_size": len(file)}


@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile] = File(description="A file read as Uploadfile")):
    if not files:
        return {"message": "No upload file sent"}
    return {"filename": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/all_files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form(),
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
