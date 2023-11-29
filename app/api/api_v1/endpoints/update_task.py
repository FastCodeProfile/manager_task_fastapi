from fastapi import APIRouter, HTTPException, Depends

from app.api import depends
from app.database import Database
from app.schemas import TaskSchemeAdd

router = APIRouter()


# Обновление информации о задаче
@router.put('/{task_id}')
async def update_task(task_id: int, task: TaskSchemeAdd, db: Database = Depends(depends.get_db)):
    task_in_db = await db.task.get(task_id)
    if task_in_db:
        await db.task.update(task_id, **task.model_dump())
        await db.session.commit()
        return {'message': 'Task updated successfully'}
    raise HTTPException(status_code=404, detail='Task not found')
