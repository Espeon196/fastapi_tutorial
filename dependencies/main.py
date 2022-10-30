from http.client import HTTPException
from typing import Optional

from fastapi import Depends, FastAPI, Cookie, Header, HTTPException


async def all_dependencies():
    print("Called")


app = FastAPI(dependencies=[Depends(all_dependencies)])


"""
async def common_parameters(
    q: Optional[str] = None, skip: int = 0, limit: int = 100,
):
    return {"q": q, "skip": skip, "limit": limit}
"""

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    return commons


@app.get("/users/")
async def read_users(commons: CommonQueryParams = Depends()):
    return commons


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: Optional[str] = Depends(query_extractor),
    last_query: Optional[str] = Cookie(default=None),
):
    if not q:
        return last_query
    return q


@app.get("/query/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/secrets/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]
