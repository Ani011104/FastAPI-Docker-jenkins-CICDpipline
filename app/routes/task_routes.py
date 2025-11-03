import fastapi import APIRouter, HTTPException
from app.models.task_models import Task
from app.database import connections
from app.controllers import task_controller

router = APIRouter()

@router.post("/tasks")
async def create_task(task: Task):
    try:
        result = task_controller.create_task(task)
        return {"message": "Task created successfully", "task": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/tasks")
async def get_tasks():
    try:
        tasks = task_controller.get_tasks()
        return {"tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    try:
        task_controller.delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.put("/tasks/{task_id}")
# async def update_task(task_id: str, task: Task):
#     try:
#         task_controller.update_task(task_id, task)
#         return {"message": "Task updated successfully", "task": task}