from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)