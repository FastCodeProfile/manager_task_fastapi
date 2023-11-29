import datetime as dt

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.schemas.tasks import TaskPriority, TaskStatus
from .base import Base


class Task(Base):
    name: Mapped[str] = mapped_column(sa.String, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=False)
    priority: Mapped[TaskPriority] = mapped_column(sa.Enum(TaskPriority), unique=False, nullable=False)
    status: Mapped[TaskStatus] = mapped_column(sa.Enum(TaskStatus), unique=False, nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(sa.DateTime(timezone=True), default=dt.datetime.now)
    update_at: Mapped[dt.datetime] = mapped_column(sa.DateTime(timezone=True), onupdate=dt.datetime.now,
                                                   default=dt.datetime.now)

    def __repr__(self):
        return f"Task:{self.id=}"
