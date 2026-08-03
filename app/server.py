import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import transaction, category

app = FastAPI()

origins = ["http://localhost:3000"]

frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    origins.append(frontend_url.rstrip("/"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction.router, prefix="/api")
app.include_router(category.router, prefix="/api")