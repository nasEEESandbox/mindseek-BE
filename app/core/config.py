import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "MindSeek API"
    API_VERSION: str = "v1"

    # Database Settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite3")

    # Security Keys
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # Token expiry time

    # OpenAI API Key
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    class Config:
        case_sensitive = True


# Create a single instance of Settings
settings = Settings()
