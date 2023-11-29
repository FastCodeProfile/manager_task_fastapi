from fastapi import APIRouter, Depends

from app.api import depends
from app.database import Database
from app.worker import send_email
from app.schemas import TaskSchemeAdd, TaskPriority

router = APIRouter()


# Создание новой задачи
@router.post('/')
async def create_task(task: TaskSchemeAdd, db: Database = Depends(depends.get_db)):
    task_in_db = await db.task.new(**task.model_dump())
    await db.session.commit()
    if task.priority == TaskPriority.VERY_IMPORTANT:
        # Асинхронное выполнение задачи с высоким приоритетом
        send_email.delay(task_in_db)
    return {'message': 'Task created successfully'}
