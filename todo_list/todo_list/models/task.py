from todo_list.models.user import User
from enum import Enum
from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship


table_registry = registry()


class TaskStatus(str, Enum):
    doing = 'doing'
    finished = 'finished'


@table_registry.mapped_as_dataclass
class Task:
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    description: Mapped[str] 
    status: Mapped[TaskStatus]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey(User.__table__.c.id))
    user: Mapped[User] = relationship("User", back_populates="tasks")