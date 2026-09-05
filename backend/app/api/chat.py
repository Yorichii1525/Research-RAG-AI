from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.rag.pipeline import answer_query

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("", response_model=ChatResponse)
async def chat_query(request: ChatRequest):
    try:
        return answer_query(request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
