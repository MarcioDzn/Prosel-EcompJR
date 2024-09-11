from enum import Enum
from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship


table_registry = registry()


class TaskStatus(str, Enum):
    doing = 'doing'
    finished = 'finished'


class UserType(str, Enum):
    user = "user"
    administrator = "administrator"


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    type: Mapped[UserType]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

    tasks: Mapped[list["Task"]] = relationship("Task", init=False, back_populates="user", cascade='all, delete-orphan')


@table_registry.mapped_as_dataclass
class Task:
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    description: Mapped[str] 
    status: Mapped[TaskStatus]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey(User.__table__.c.id))
    user: Mapped[User] = relationship("User", init=False, back_populates="tasks")