from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import Body, FastAPI, Cookie

app = FastAPI()


@app.put("/items/{item_id}")
async def put_items(
    item_id: UUID,
    start_datetime: datetime = Body(),
    end_datetime: datetime = Body(),
    repeat_at: time = Body(),
    process_after: timedelta = Body(),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie()):
    return {"ads_id": ads_id}
