import datetime as dt
from enum import Enum

from pydantic import BaseModel


class TaskStatus(int, Enum):
    IN_PROCESS = 0
    COMPLETED = 1


class TaskPriority(int, Enum):
    NOT = 0
    IMPORTANT = 1
    VERY_IMPORTANT = 2


class TaskScheme(BaseModel):
    id: int = 0
    name: str = "Задача №1"
    description: str = "Описание задачи"
    priority: TaskPriority = TaskPriority.NOT
    status: TaskStatus = TaskStatus.IN_PROCESS
    created_at: str = dt.datetime.now()
    update_at: str = dt.datetime.now()


class TaskSchemeAdd(BaseModel):
    name: str = "Задача №1"
    description: str = "Описание задачи"
    priority: TaskPriority = TaskPriority.NOT
    status: TaskStatus = TaskStatus.IN_PROCESS
