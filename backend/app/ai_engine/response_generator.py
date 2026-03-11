import logging
from app.config import settings
from app.services.sentiment_service import analyze_sentiment

# we import the newer client interface; the old ``openai.ChatCompletion`` was
# removed in openai>=1.0, so use the ``OpenAI`` helper instead.
try:
    from openai import OpenAI
    _client = OpenAI(api_key=settings.OPENAI_API_KEY)
except ImportError:
    # fallback if user stuck with old library version; the tests will bypass
    # either way by monkeypatching.
    import openai as _legacy
    _client = _legacy


logger = logging.getLogger(__name__)


def generate_response(review: str) -> str:
    """Return a text response for *review* using the LLM.

    This helper swallows any underlying exceptions and returns a simple
    string if the call fails, avoiding 500 errors bubbling up to the API.
    """

    if not settings.OPENAI_API_KEY:
        return "<api-key-not-configured>"

    sentiment = analyze_sentiment(review)

    prompt = (
        f"Customer Review: {review}\n"
        f"Sentiment: {sentiment}\n\n"
        "Write a professional response from a business."
    )

    try:
        # the new client exposes ``chat.completions.create``; the legacy
        # object behaves like ``openai.ChatCompletion`` so either path works.
        if hasattr(_client, "chat"):
            result = _client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
            )
            return result.choices[0].message.content
        else:
            # legacy path
            res = _client.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
            )
            return res.choices[0].message.content
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception("failed to generate response")
        return "<error-generating-response>"