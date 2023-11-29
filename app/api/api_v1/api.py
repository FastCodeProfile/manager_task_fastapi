from fastapi import APIRouter

from app.api.api_v1.endpoints import create_task, get_tasks, get_task_details, update_task

api_router = APIRouter(prefix="/tasks", tags=["tasks"])
api_router.include_router(create_task.router)
api_router.include_router(get_tasks.router)
api_router.include_router(get_task_details.router)
api_router.include_router(update_task.router)
