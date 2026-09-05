from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str

class SourceCitation(BaseModel):
    filename: str
    page: int
    chunk_id: Optional[str] = None
    content: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceCitation]
