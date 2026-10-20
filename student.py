from database import base
from sqlalchemy import Column,String,Integer

class Student(base):
    __tablename__="student"
    __table_arg__={"schema:training"}
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    
    