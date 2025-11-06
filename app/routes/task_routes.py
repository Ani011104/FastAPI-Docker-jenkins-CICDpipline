# app/routes/task_routes.py
from fastapi import APIRouter, HTTPException
from app.models.task_models import Task
from app.controllers import task_controllers

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task):
    try:
        result = task_controllers.create_task(task)
        return {"message": "Task created successfully", "task_id": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tasks")
def get_tasks():
    try:
        tasks = task_controllers.get_tasks()
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found")
        return {"tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        task_controllers.delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
