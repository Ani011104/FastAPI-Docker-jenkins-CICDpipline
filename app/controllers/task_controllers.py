# app/controllers/task_controller.py
from app.models.task_models import Task
from app.database.connections import collection
from bson import ObjectId

def create_task(task: Task):
    try:
        result = collection.insert_one(task.model_dump())
        return str(result.inserted_id)
    except Exception as e:
        raise Exception(f"Error creating task: {e}")

def get_tasks():
    try:
        tasks = []
        for task in collection.find():
            task["_id"] = str(task["_id"])
            tasks.append(task)
        return tasks
    except Exception as e:
        raise Exception(f"Error getting tasks: {e}")

def delete_task(task_id: str):
    try:
        collection.delete_one({"_id": ObjectId(task_id)})
    except Exception as e:
        raise Exception(f"Error deleting task: {e}")
