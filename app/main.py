from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.todos import router as todo_router

app = FastAPI(
    title="Todo APP API",
    description="Backend API for Todo App",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://webmcp-todo-app.vercel.app",
        "https://webmcp-todo-app-git-main-saurabh-bakolias-projects.vercel.app",
        "https://webmcp-todo-r5ejhjzpi-saurabh-bakolias-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)


@app.get("/")
def root():
    return {"message": "Todo API is running"}
