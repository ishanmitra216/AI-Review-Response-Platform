from sqlalchemy import Column, Integer, String
from app.database import Base

class Response(Base):

    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    review_id = Column(Integer)
    response_text = Column(String)