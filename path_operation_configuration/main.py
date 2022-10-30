from enum import Enum
from typing import Optional

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(ge=0)
    tax: Optional[float] = Field(default=None)
    tags: set[str] = set()


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    summary="Create an item",
    #description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    ## Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=[Tags.items], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
