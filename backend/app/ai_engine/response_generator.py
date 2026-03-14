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


def _fallback_response(review: str, sentiment: str) -> str:
    """Return a safe local response when LLM access is unavailable."""

    if sentiment == "positive":
        return (
            "Thank you for your kind feedback. We are glad you had a great "
            "experience and look forward to serving you again soon."
        )
    if sentiment == "negative":
        return (
            "Thank you for sharing your feedback. We are sorry your experience "
            "did not meet expectations, and we would like to make it right. "
            "Please contact us so we can follow up directly."
        )
    return (
        "Thank you for your review. We appreciate your feedback and will use "
        "it to keep improving our service."
    )


def generate_response(review: str) -> str:
    """Return a text response for *review* using the LLM.

    This helper swallows any underlying exceptions and returns a simple
    string if the call fails, avoiding 500 errors bubbling up to the API.
    """

    sentiment = analyze_sentiment(review)

    if not settings.OPENAI_API_KEY:
        return _fallback_response(review, sentiment)

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
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            return result.choices[0].message.content
        else:
            # legacy path
            res = _client.ChatCompletion.create(
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            return res.choices[0].message.content
    except Exception:  # pylint: disable=broad-except
        logger.exception("failed to generate response")
        return _fallback_response(review, sentiment)