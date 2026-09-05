import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ResearchAI"
    MISTRAL_API_KEY: str = os.getenv("MISTRAL_API_KEY", "")
    CHROMA_PERSIST_DIRECTORY: str = os.getenv("CHROMA_PERSIST_DIRECTORY", "./storage/chroma")
    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY", "./storage/uploads")
    
    class Config:
        env_file = ".env"

settings = Settings()

os.makedirs(settings.CHROMA_PERSIST_DIRECTORY, exist_ok=True)
os.makedirs(settings.UPLOAD_DIRECTORY, exist_ok=True)
