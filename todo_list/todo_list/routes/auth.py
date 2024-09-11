from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException

from fastapi.security import OAuth2PasswordRequestForm
from todo_list.security import verify_password, create_token

from todo_list.models.models import User

from todo_list.schemas.token import Token

from sqlalchemy import select
from sqlalchemy.orm import Session
from todo_list.configs.database import get_session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/", status_code=HTTPStatus.OK)
def auth(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)) -> Token:
    user = session.scalar(
        select(User).where(
            User.email == form_data.username
        )
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Email ou senha inválidos"
        )
    
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Email ou senha inválidos"
        )
    
    token = create_token(data={"sub": user.email})
    
    print(token)
    return Token(access_token=token, token_type="bearer")
