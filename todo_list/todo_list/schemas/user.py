from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class UserType(str, Enum):
    user = "user"
    administrator = "administrator"


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    type: UserType


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: UserType
    created_at: datetime


class UserList(BaseModel):
    users: list[UserPublic]


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    type: UserType | None = None


