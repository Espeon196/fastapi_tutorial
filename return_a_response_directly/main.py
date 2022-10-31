from datetime import datetime
from sqlite3 import Timestamp
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    Timestamp: datetime
    description: Optional[str] = None


app = FastAPI()


@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/legacy/")
async def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")
