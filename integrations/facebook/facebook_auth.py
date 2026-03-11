import os


def authenticate_facebook():
    """Return Facebook API token from environment.
    """
    return os.getenv("FACEBOOK_API_KEY", "")