import os


def authenticate_google():
    """Return Google API key from environment.
    """
    return os.getenv("GOOGLE_API_KEY", "")