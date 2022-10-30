from typing import Optional
import aiofiles

from fastapi import BackgroundTasks, FastAPI, Depends

app = FastAPI()


async def write_notification(message):
    async with aiofiles.open("log.txt", mode="a") as email_file:
        await email_file.write(message)


def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_notification, message)


@app.post("/send_notification/{email}")
async def send_notification(
    email: str, 
    background_tasks: BackgroundTasks,
    q: str = Depends(get_query)
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_notification, message=message)
    return {"message": "Notification sent in the background"}
