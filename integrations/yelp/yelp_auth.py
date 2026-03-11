import os


def authenticate_yelp():
    """Return Yelp API key from environment (or empty string).

    This allows the auth helper to be used in production once a valid key is
    supplied via the `.env` file or environment variables.
    """
    return os.getenv("YELP_API_KEY", "")