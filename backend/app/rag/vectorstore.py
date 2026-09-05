from langchain_chroma import Chroma
from app.core.config import settings
from app.rag.embeddings import get_embedding_function

def get_vectorstore():
    return Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY,
        embedding_function=get_embedding_function(),
        collection_name="researchai_knowledge"
    )
