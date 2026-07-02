from fastapi import FastAPI, HTTPException
from datetime import datetime
import boto3
import socket

app = FastAPI()

BUCKET_NAME = "purva-internship-backup-2026"

s3 = boto3.client("s3")
@app.get("/")
def home():
    return {
        "message": "This app is runnning, CI/CD implementation done"
    }
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        s3.upload_fileobj(
            file.file,
            BUCKET_NAME,
            file.filename
        )

        return {
            "message": "File uploaded successfully",
            "filename": file.filename
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
