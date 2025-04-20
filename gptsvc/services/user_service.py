from gptsvc.models.user import User, Gender
import random

def _generate_user() -> User:
    user = User()
    user.age = random.randint(1, 100)
    user.gender = User.generate()
    
    return user

class UserService:
    # users are stored at class level
    users = []
    
    def __init__(self):
        for i in range(10):
            UserService.users.append(_generate_user())
            
    def get_users(self) -> list[User]:
        return UserService.users
    
    def add_user(self, user:User):
        id = random.randint()
        user.id = id
        UserService.users.append(user)
        
    def delete_user(self, user:User):
        for i, u in UserService.users:
            if u.id == user.id :
                UserService.users.remove(u)
        

            
    

    
   




    

