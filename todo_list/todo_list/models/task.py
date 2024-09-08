from enum import Enum
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_columm, registry

table_registry = registry()


class TaskStatus(str, Enum):
    doing = 'doing'
    finished = 'finished'


@table_registry.mapped_as_dataclass
class Task:
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_columm(init=False, primary_key=True)
    title: Mapped[str]
    description: Mapped[str] 
    status: Mapped[TaskStatus]
    created_at: Mapped[datetime] = mapped_columm(init=False, server_default=func.now())