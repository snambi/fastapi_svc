from typing import List
from fastapi import FastAPI
from gptsvc.models.item import Item

from gptsvc.routers.user_router import user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/hello")
async def get_hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("request hello received")
    return {"message": "Hello World!!!"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    """_summary_

    Returns:
        _type_: _description_
    """
    print("request items received")
    return []