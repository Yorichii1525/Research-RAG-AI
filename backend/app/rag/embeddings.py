import os
from google import genai
from google.genai import types
from chromadb.api.types import EmbeddingFunction, Documents, Embeddings
from app.core.config import settings

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model_name: str = "gemini-embedding-2", dimensions: int = 768):
        api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.dimensions = dimensions

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = []
        for text in input:
            formatted_text = f"title: none | text: {text}"
            response = self.client.models.embed_content(
                model=self.model_name,
                contents=formatted_text,
                config=types.EmbedContentConfig(
                    output_dimensionality=self.dimensions
                )
            )
            embeddings.append(response.embeddings[0].values)
        return embeddings

_embedding_instance = None

def get_embedding_function():
    global _embedding_instance
    if _embedding_instance is None:
        _embedding_instance = GeminiEmbeddingFunction()
    return _embedding_instance
