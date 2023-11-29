from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from app.core.config import settings
from .repositories import TaskRepo


def create_async_engine(url: URL | str) -> AsyncEngine:
    return _create_async_engine(url=url, echo=False, pool_pre_ping=True)


engine = create_async_engine(settings.pg_dns)


class Database:
    task: TaskRepo

    session: AsyncSession

    def __init__(
            self,
            session: AsyncSession,
            task: TaskRepo = None,
    ):
        self.session = session
        self.task = task or TaskRepo(session=session)
