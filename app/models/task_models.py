# app/models/task_models.py
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    user_id: str
    title: str
    description: Optional[str] = None
    completed: bool = False


