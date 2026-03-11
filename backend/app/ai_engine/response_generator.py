import openai
from app.config import settings
from app.services.sentiment_service import analyze_sentiment

openai.api_key = settings.OPENAI_API_KEY


def generate_response(review):
    """Build a response using OpenAI.

    If the ``OPENAI_API_KEY`` is not set the function returns a placeholder
    string rather than raising an error; this makes development and testing
    easier.
    """

    if not settings.OPENAI_API_KEY:
        # demonstrative stub (see tests which monkeypatch the OpenAI call)
        return "<api-key-not-configured>"

    sentiment = analyze_sentiment(review)

    prompt = f"""
    Customer Review: {review}
    Sentiment: {sentiment}

    Write a professional response from a business.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content