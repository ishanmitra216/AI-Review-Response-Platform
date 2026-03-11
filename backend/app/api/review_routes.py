from fastapi import APIRouter
from app.schemas.review_schema import ReviewRequest
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()


@router.post("/analyze")
def analyze_review(review: ReviewRequest):
    """Return sentiment for a single review.

    This endpoint is used by the frontend and test harness. It currently
    uses the ``TextBlob`` based sentiment analyzer in
    :mod:`app.services.sentiment_service`.
    """

    sentiment = analyze_sentiment(review.text)

    return {
        "review": review.text,
        "sentiment": sentiment
    }