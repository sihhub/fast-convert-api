from fastapi import APIRouter, FastAPI, File, Form, HTTPException, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

from routes import xml_to_html_router  # routes 폴더에서 불러온 라우트 사용

app = FastAPI(
    docs_url="/docs",
    openapi_url="/openapi.json",
    title="fast Convert API",
    description="fast Convert API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# 기본 경로
@app.get("/", tags=["Root"], summary="Root")
async def root():
    return {"message": "Welcome to the Fast Convert API!"}


app.include_router(xml_to_html_router, prefix="/xml-to-html", tags=["XML, HTML"])
