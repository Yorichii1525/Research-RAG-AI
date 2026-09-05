from app.rag.vectorstore import get_vectorstore

def get_mmr_retriever(k: int = 4, fetch_k: int = 10, lambda_mult: float = 0.5):
    return get_vectorstore().as_retriever(
        search_type="mmr",
        search_kwargs={"k": k, "fetch_k": fetch_k, "lambda_mult": lambda_mult}
    )
