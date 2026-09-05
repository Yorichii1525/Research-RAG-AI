from langchain_community.embeddings import HuggingFaceEmbeddings

_embedding_instance = None

def get_embedding_function():
    global _embedding_instance
    if _embedding_instance is None:
        _embedding_instance = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return _embedding_instance
