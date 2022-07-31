import json
from pathlib import Path


# Simple Fastapi server
from fastapi import FastAPI, Request, Form, Depends, APIRouter, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from youtubesearchpython.__future__ import VideosSearch

BASE_PATH = Path(__file__).parent.parent
BUILD_PATH = Path(BASE_PATH / "frontend/build/")
STATIC_PATH = BUILD_PATH / "static"

app = FastAPI(title="Youtube Proxy Server")
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
templates = Jinja2Templates(directory=BUILD_PATH)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/ping/", response_class=JSONResponse)
async def ping():
    return {"message": "pong"}

@app.post("/search/", response_class=JSONResponse)
async def search(search: str = Form()):
    results = await VideosSearch(search, limit = 10).next()
    return results["result"]

