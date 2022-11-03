from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/headers_and_object/")
async def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
