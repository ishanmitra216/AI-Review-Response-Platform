from fastapi import APIRouter
from app.schemas.review_schema import ReviewRequest
from app.ai_engine.response_generator import generate_response

router = APIRouter()


@router.post("/generate")
def generate_ai_response(review: ReviewRequest):

    response = generate_response(review.text)

    return {
        "review": review.text,
        "response": response
    }