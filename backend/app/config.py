import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "AI Review Response Platform"
    # only required if you are running the database backend
    DATABASE_URL = os.getenv("DATABASE_URL")

    # AI / LLM provider.  you must set this to a valid OpenAI API key for the
    # response generator to work.
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # optional third‑party platform tokens – the integration modules will fall
    # back to a no‑op implementation if these are not provided.
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    YELP_API_KEY = os.getenv("YELP_API_KEY")
    FACEBOOK_API_KEY = os.getenv("FACEBOOK_API_KEY")

settings = Settings()