from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from todo_list.models.user import User

from sqlalchemy import select
from sqlalchemy.orm import Session
from todo_list.configs.database import get_session

from todo_list.schemas.user import UserCreate, UserPublic, UserList

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", status_code=HTTPStatus.CREATED)
def create_user(user: UserCreate, session: Session = Depends(get_session)) -> UserPublic:
    # verifica se já existe um usuário com o email
    db_user = session.scalar(
        select(User).where(
            user.email == User.email
        )
    )

    # tratamento de violação de unicidade
    if (db_user):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="E-mail já cadastrado!")

    db_user = User(name=user.name, email=user.email, password=user.password, type=user.type)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get("/", status_code=HTTPStatus.OK)
def get_users(session: Session = Depends(get_session)) -> UserList:
    users = session.scalars(
        select(User)
    ).all()

    return {"users": users}