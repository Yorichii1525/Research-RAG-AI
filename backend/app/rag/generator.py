import os
from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_mistral_llm():
    key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is missing.")
    return ChatGoogleGenerativeAI(
        google_api_key=key,
        model="gemini-3.1-flash-lite",
        temperature=0.1
    )
