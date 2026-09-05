import os, shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.config import settings
from app.rag.ingestion import process_pdf

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF allowed")
    path = os.path.join(settings.UPLOAD_DIRECTORY, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"message": "Uploaded", "data": process_pdf(path, file.filename)}
