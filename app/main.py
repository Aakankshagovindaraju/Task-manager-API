from fastapi import FastAPI
from .database import engine, Base
from .routers import users, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A production-ready REST API for managing tasks with JWT authentication",
    version="1.0.0"
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