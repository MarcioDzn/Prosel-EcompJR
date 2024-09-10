from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from todo_list.models.models import User

from sqlalchemy import select, update
from sqlalchemy.orm import Session
from todo_list.configs.database import get_session

from todo_list.schemas.user import UserCreate, UserPublic, UserList, UserUpdate
from todo_list.schemas.message import Message

from todo_list.security import *

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

    hashed_password = hash_pasword(user.password)

    db_user = User(name=user.name, email=user.email, password=hashed_password, type=user.type)

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


@router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int, session: Session = Depends(get_session)) -> UserPublic:
    db_user = session.scalar(
        select(User).where(
            User.id == user_id
        )
    )

    if (not db_user):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")
    
    return db_user


@router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int, session: Session = Depends(get_session)) -> Message:
    db_user = session.scalar(
        select(User).where(
            User.id == user_id
        )
    )

    if (not db_user):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")

    session.delete(db_user)
    session.commit()

    return {"message": "Usuário deletado com sucesso"}


@router.patch("/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(get_session)) -> UserPublic:
    db_user = session.scalar(
        select(User).where(
            User.id == user_id
        )
    )

    if (not db_user):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")
    

    update_data = user.dict(exclude_unset=True)

    # verifica se o usuário quer editar o email
    if 'email' in update_data:
        # se sim verifica se o email já existe
        db_user_email = session.scalar(
            select(User).where(
                user.email == User.email
            )
        )

        if (db_user_email):
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="E-mail já cadastrado!")

    if (update_data):
        stmt = update(User).where(User.id == user_id).values(**update_data)

        session.execute(stmt)
        session.commit()
        session.refresh(db_user)
    
    return db_user
