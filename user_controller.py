from fastapi import APIRouter,Depends
from schema import UserCreateRequest
from database import get_db
from service import UserService

router=APIRouter(
    prefix="/user" ,
)

@router.post("/creat")
def create_user(user_payload:UserCreateRequest,db=Depends(get_db)):
    service=UserService()
    service.create_user(db,user_payload)
    