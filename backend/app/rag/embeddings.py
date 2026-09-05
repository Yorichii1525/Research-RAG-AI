import os
from typing import List
from langchain_core.embeddings import Embeddings
from google import genai
from google.genai import types
from app.core.config import settings

class GeminiEmbeddings(Embeddings):
    def __init__(self, model_name: str = "gemini-embedding-2", dimensions: int = 768):
        api_key = settings.GEMINI_API_KEY or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing.")
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.dimensions = dimensions

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
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

    def embed_query(self, text: str) -> List[float]:
        formatted_text = f"task: search result | query: {text}"
        response = self.client.models.embed_content(
            model=self.model_name,
            contents=formatted_text,
            config=types.EmbedContentConfig(
                output_dimensionality=self.dimensions
            )
        )
        return response.embeddings[0].values

_embedding_instance = None

def get_embedding_function():
    global _embedding_instance
    if _embedding_instance is None:
        _embedding_instance = GeminiEmbeddings()
    return _embedding_instance
