from fastapi import APIRouter, Depends, HTTPException
from gptsvc.models.user import User,Gender
from gptsvc.services.user_service import UserService
from gptsvc.controllers.user_controller import UserController
import random

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

user_controller:UserController = None

def get_user_service():
    return UserService()

def get_user_controller(service:UserService = Depends(get_user_service)):
    if(user_controller == None):
        user_controller = UserController(service)
    
    return user_controller
    

@user_router.get("/", response_model=list[User])
async def get_users(controller:UserController = Depends(get_user_controller)):
    return controller.get_users()

