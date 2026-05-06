from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import users, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A production-ready REST API for managing tasks with JWT authentication",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
        "http://localhost:5177",
        "http://localhost:5178",
        "https://task-manager-frontend-beige-tau.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API is running",
        "docs": "/docs",
        "version": "1.0.0"
    }