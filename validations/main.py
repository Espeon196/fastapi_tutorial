from typing import Optional
from fastapi import FastAPI, Query
from pydantic import Required, constr


app = FastAPI()


StringConstr = constr(min_length=3, max_length=50, regex=r"^[a-z]*$")

@app.get("/items/")
async def read_items(
    q: Optional[list[StringConstr]] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database",
    ),
    r: str = Query(default=Required, max_length=50)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    results.update({"r": r})
    return results
