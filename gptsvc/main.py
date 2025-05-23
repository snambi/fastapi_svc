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
        
@app.get("/hello")
async def get_hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    logger.info("hello received")
    return {"message": "Hello World!!!"}


@app.get("/healthz")
@app.get("/health")
@app.get("/")
def health():
    return {"status": "ok"}