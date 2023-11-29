from fastapi import APIRouter, HTTPException, Depends

from app.api import depends
from app.database import Database

router = APIRouter()


# Просмотр деталей задачи
@router.get('/{task_id}')
async def get_task_details(task_id: int, db: Database = Depends(depends.get_db)):
    task = await db.task.get(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail='Task not found')
