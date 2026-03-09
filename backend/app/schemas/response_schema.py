from pydantic import BaseModel

class ResponseSchema(BaseModel):

    review_id: int
    response_text: str