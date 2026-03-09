import openai
from app.config import settings
from app.services.sentiment_service import analyze_sentiment

openai.api_key = settings.OPENAI_API_KEY


def generate_response(review):

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