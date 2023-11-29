import datetime as dt

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.tasks import TaskPriority, TaskStatus
from .abstract import Repository
from ..models import Task


class TaskRepo(Repository[Task]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Task, session=session)

    async def new(
            self,
            name: str,
            description: str,
            priority: TaskPriority,
            status: TaskStatus,
    ) -> Task:
        new_task = await self.session.merge(
            Task(
                name=name,
                description=description,
                priority=priority,
                status=status,
            )
        )
        return new_task

    async def get_many_by_status_priority(self, status: TaskStatus, priority: TaskPriority) -> list[Task]:
        tasks = await self.get_many(and_(Task.status == status, Task.priority == priority))
        return tasks
