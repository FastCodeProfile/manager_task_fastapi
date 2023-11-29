from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Database
from app.database.database import engine


async def get_db(request: Request = None) -> Database:
    if request:
        return request.state.db
    else:
        async with AsyncSession(bind=engine, expire_on_commit=False) as session:
            return Database(session)
