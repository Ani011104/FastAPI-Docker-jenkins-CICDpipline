# app/main.py
from fastapi import FastAPI
from app.routes import task_routes

app = FastAPI()

app.include_router(task_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
