from sqlalchemy import Column, Integer, String
from app.database import Base

class Business(Base):

    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    name = Column(String)