from sqlalchemy import Column, Integer, String
from app.database import Base

class Review(Base):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    rating = Column(Integer)