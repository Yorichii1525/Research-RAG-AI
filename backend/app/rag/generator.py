from langchain_mistralai import ChatMistralAI
from app.core.config import settings

def get_mistral_llm():
    key = settings.MISTRAL_API_KEY
    if not key or key == "your_mistral_api_key_here":
        raise ValueError("MISTRAL_API_KEY is missing. Please set your key in researchai/backend/.env")
    return ChatMistralAI(
        api_key=key,
        model="open-mistral-7b",
        temperature=0.1
    )
