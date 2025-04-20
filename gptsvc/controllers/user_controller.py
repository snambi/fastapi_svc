from gptsvc.services.user_service import UserService
from gptsvc.models.user import User

class UserController:
    def __init__(self, user_service:UserService):
        self.service = user_service
        
    def get_users(self) -> list[User]:
        return self.service.get_users()