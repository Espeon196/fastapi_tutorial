from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(default=None, max_length=100)
    price: float = Field(gt=0)
    tax: float = Field(default=10, ge=0, le=100)
    tags: set[str] = set()


items = {
    "foo": {"name": "Foo", "price": 50.3},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
