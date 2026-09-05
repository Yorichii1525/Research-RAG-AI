import uuid
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vectorstore import get_vectorstore

def process_pdf(file_path: str, original_filename: str):
    loader = PyPDFLoader(file_path)
    raw_docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(raw_docs)
    doc_id = str(uuid.uuid4())
    for idx, chunk in enumerate(chunks):
        chunk.metadata["document_id"] = doc_id
        chunk.metadata["filename"] = original_filename
        chunk.metadata["chunk_id"] = f"{doc_id}_{idx}"
        if "page" in chunk.metadata:
            chunk.metadata["page"] = int(chunk.metadata["page"]) + 1
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    return {"document_id": doc_id, "filename": original_filename, "total_pages": len(raw_docs), "total_chunks": len(chunks)}
