from enum import Enum
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_columm, registry

table_registry = registry()


class UserType(str, Enum):
    user = "user"
    administrator = "administrator"


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_columm(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_columm(unique=True)
    password: Mapped[str]
    type: Mapped[UserType]
    created_at: Mapped[datetime] = mapped_columm(init=False, server_default=func.now())