from app.rag.retriever import get_mmr_retriever
from app.rag.generator import get_mistral_llm
from app.rag.prompts import RAG_PROMPT

def answer_query(query: str):
    retriever = get_mmr_retriever()
    retrieved_docs = retriever.invoke(query)
    if not retrieved_docs:
        return {"answer": "I could not find the answer in the document.", "sources": []}
    
    context_blocks = [doc.page_content for doc in retrieved_docs]
    context_str = "\n\n".join(context_blocks)
    
    prompt_text = RAG_PROMPT.format(context=context_str, question=query)
    llm = get_mistral_llm()
    response = llm.invoke(prompt_text)
    
    content = getattr(response, "content", response)
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
            elif hasattr(item, "text"):
                parts.append(item.text)
            else:
                parts.append(str(item))
        answer_text = "".join(parts)
    else:
        answer_text = str(content)
    
    sources = []
    for doc in retrieved_docs:
        sources.append({
            "filename": doc.metadata.get("filename", "Unknown Document"),
            "page": doc.metadata.get("page", 1),
            "content": doc.page_content[:300] + "..."
        })
        
    return {
        "answer": answer_text,
        "sources": sources
    }
