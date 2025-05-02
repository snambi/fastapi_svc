from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

import requests
import json

from gptsvc.config.logging_config import initialize_logger
initialize_logger()

logger = logging.getLogger(__name__)
logger.info("gptsvc initializing")

from gptsvc.models.item import Item
from gptsvc.routers.user_router import user_router


async def on_startup():
    logger.info("running startup tasks")
    
async def on_shutdown():
    logger.info("shutting down\n\n")
 
@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()
    try:
        yield
    finally:
        await on_shutdown()
    

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
    
@app.post("/chat")
async def chat(input:str):
    data = {
                "model": "mistral-large-latest",
                "messages": [
                {
                    "role": "user",
                    "content": f"{input}"
                }
                ]
            }
    
    headers = {
                "Content-Type": "application/json",
                "Accept" : "application/json",
                "Authorization" : "Bearer D23yxyESwEK9bo3fG2iiSWMtvLy5N45e"
            }
    response = requests.post("https://api.mistral.ai/v1/chat/completions", 
                             data=json.dumps(data), 
                             headers=headers)
    
    logger.debug("f{resposne.status_code}")
    return {"result": f"{response.json()}"}
    

@app.get("/hello")
async def get_hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    logger.info("hello received")
    return {"message": "Hello World!!!"}

