from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    doing = "doing"
    finished = "finished"


class TaskCreate(BaseModel):
    title: str
    description: str
    status: TaskStatus


class TaskPublic(BaseModel):
    id: int 
    title: str
    description: str
    status: TaskStatus
    created_at: datetime


class TaskList(BaseModel):
    tasks: list[TaskPublic]


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None