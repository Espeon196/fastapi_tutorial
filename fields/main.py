from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        default=None, title="The description of the item", max_length=300,
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: set[str] = set()
    images: Optional[list[Image]] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 42.5,
                "tax": 3.5,
                "tags": [
                    "new"
                ],
                "images": [
                    {
                        "url": "http://127.0.0.1:8080/docs.png",
                        "name": "sample image"
                    }
                ]
            }
        }


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image] = Body(
    example=[
        {
            "url": "http://images.com/image.png",
            "name": "image.png",
        },
    ]
)):
    return images
