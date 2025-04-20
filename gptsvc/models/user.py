from enum import Enum
from pydantic import BaseModel
import random

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    

            
    
class User(BaseModel):
    id:int = 0
    name:str = None
    age:int = 0
    retired:bool = False
    gender:Gender = Gender.OTHER
    
    model_config = {
        "frozen": True
    }

    @staticmethod
    def generate() -> Gender :        
        match random.randint(1, 3, 1):
            case 1:
                return Gender.MALE
            case 2:
                return Gender.FEMALE
            case 3:
                return Gender.OTHER
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, retired: {self.retired}, gender: {self.gender}"
    
    def say(x: tuple[str]) -> str:
        print("hello")