import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "AI Review Response Platform"
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()