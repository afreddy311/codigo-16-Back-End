from app import db 
from sqlalchemy import Column,Integer,String
from dataclasses import dataclass

@dataclass
class AreaModel (db.Model):
    id: int
    name:str

    __tablename__='area'
    __table_args__= {'schema': 'areas'}#para trabajar con varios esquemas

    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50), nullable=False)







