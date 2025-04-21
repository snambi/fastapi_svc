from fastapi import APIRouter, Depends, HTTPException
import random, logging

from gptsvc.models.user import User,Gender
from gptsvc.services.user_service import UserService
from gptsvc.controllers.user_controller import UserController

logger = logging.getLogger(__name__)

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

user_controller:UserController = None

def get_user_service():
    return UserService()

def get_user_controller(service:UserService = Depends(get_user_service)):
    global user_controller
    if(user_controller is None):    
        user_controller = UserController(service)
    
    return user_controller
    

@user_router.get("/", response_model=list[User])
async def get_users(controller:UserController = Depends(get_user_controller)):
    return controller.get_users()

