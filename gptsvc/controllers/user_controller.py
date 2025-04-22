import logging

from gptsvc.services.user_service import UserService
from gptsvc.models.user import User

logger = logging.getLogger(__name__)

class UserController:
    def __init__(self, user_service:UserService):
        self.service = user_service
        
    def get_users(self) -> list[User]:
        logger.debug("request received on get_users()")
        return self.service.get_users()