from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="Email Replier API",
    description="Gera respostas automáticas para e-mails usando OpenAI",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://emailreplier.onrender.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")