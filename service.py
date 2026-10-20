from repository import UserRepository
from schema import UserCreateRequest
from sqlalchemy.orm import Session
from user import User

class UserService:
    def __init__(self):
        self.user_repository=UserRepository()
        
    def create_user(self,db: Session, user_payload:UserCreateRequest):
        user=User(name=user_payload.name,
                email=user_payload.email,
                age=user_payload.age
                )
        self.user_repository.create_user(db , user)
        