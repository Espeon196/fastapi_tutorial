from typing import Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(default=None)):
    return {"User-Agent": user_agent}


@app.get("/list_headers/")
async def read_headers(x_token: Optional[list[str]] = Header(default=None)):
    return {"X-Token values": x_token}
