from functools import lru_cache

from fastapi import FastAPI, Depends

from .config import Settings


app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()

@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return settings