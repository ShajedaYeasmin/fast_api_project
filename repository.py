from sqlalchemy.orm import Session
from schema import UserCreateRequest
from user import User


class UserRepository:

    def create_user(self,db: Session, user_payload: User):
        db.add(user_payload)
        db.commit()

    def get_user_by_id(self, db: Session, id: int):
        db_user = db.query(User).filter(User.id == id).first()
        return db_user
    
    def get_all_user(self, db:Session):
        db_users= db.query(User).all()


