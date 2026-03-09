from app.services.sentiment_service import analyze_sentiment

def test_positive():

    text = "Great food and amazing service"

    assert analyze_sentiment(text) == "positive"