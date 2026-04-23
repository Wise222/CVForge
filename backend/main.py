# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import cv, documents, pdf

app = FastAPI(
    title="CVForge Pro API",
    description="Africa Most Advanced AI Career Document Builder",
    version="3.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(cv.router, prefix="/api/cv", tags=["CV"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(pdf.router, prefix="/api/pdf", tags=["PDF"])

@app.get("/")
def root():
    return {"message": "CVForge Pro API v3.0 is running", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy", "model": "cvforge-model-v3"}
