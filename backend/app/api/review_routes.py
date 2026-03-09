from fastapi import APIRouter
from app.schemas.review_schema import ReviewRequest
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()


@router.post("/analyze")
def analyze_review(review: ReviewRequest):

    sentiment = analyze_sentiment(review.text)

    return {
        "review": review.text,
        "sentiment": sentiment
    }