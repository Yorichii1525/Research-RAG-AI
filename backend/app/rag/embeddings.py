from langchain_mistralai import MistralAIEmbeddings
from app.core.config import settings

_embedding_instance = None

def get_embedding_function():
    global _embedding_instance
    if _embedding_instance is None:
        key = settings.MISTRAL_API_KEY
        if not key or key == "your_mistral_api_key_here":
            raise ValueError("MISTRAL_API_KEY is missing.")
        _embedding_instance = MistralAIEmbeddings(
            api_key=key,
            model="mistral-embed"
        )
    return _embedding_instance
