from fastapi import FastAPI, HTTPException
from datetime import datetime
import socket

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "This app is runnning"
    }
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

