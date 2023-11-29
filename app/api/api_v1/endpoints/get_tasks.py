from fastapi import APIRouter, Depends

from app.api import depends
from app.database import Database
from app.schemas import TaskPriority, TaskStatus

router = APIRouter()


# Просмотр списка задач
@router.get('/')
async def get_tasks(status: TaskStatus, priority: TaskPriority, db: Database = Depends(depends.get_db)):
    tasks = await db.task.get_many_by_status_priority(status, priority)
    return tasks
