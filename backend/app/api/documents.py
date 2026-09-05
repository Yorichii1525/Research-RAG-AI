import os, shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.config import settings
from app.rag.ingestion import process_pdf

router = APIRouter(prefix="/api/documents", tags=["documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = os.path.join(settings.UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        result = process_pdf(file_path, file.filename)
        return {"message": "Document processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
