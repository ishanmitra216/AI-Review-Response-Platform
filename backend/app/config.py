import os
from pathlib import Path
from dotenv import load_dotenv

# ensure we load the .env file sitting in the backend directory rather than
# relying on the current working directory.  ``config.py`` lives under
# backend/app; a single parent gives us the backend folder itself.
env_path = Path(__file__).parents[1] / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    # fall back to default behaviour (search CWD)
    load_dotenv()


class Settings:
    PROJECT_NAME = "AI Review Response Platform"
    # only required if you are running the database backend
    DATABASE_URL = os.getenv("DATABASE_URL")

    # AI / LLM provider.  you must set this to a valid OpenAI API key for the
    # response generator to work.
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # default to a widely available model so student/free tiers work out of box.
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # optional third‑party platform tokens – the integration modules will fall
    # back to a no‑op implementation if these are not provided.
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    YELP_API_KEY = os.getenv("YELP_API_KEY")
    FACEBOOK_API_KEY = os.getenv("FACEBOOK_API_KEY")


settings = Settings()