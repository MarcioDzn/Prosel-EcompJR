from http import HTTPStatus
from datetime import timedelta, datetime, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

import jwt
from jwt.exceptions import InvalidTokenError

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session
from todo_list.configs.database import get_session
from todo_list.models.models import User
from todo_list.schemas.token import TokenData

SECRET_KEY="9279843e857e59924bffb1f77343f936256e4951ebba20a102d2998a5eb316b3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def create_token(data: dict, expires_delta: timedelta | None = None):
    data_to_encode = data.copy()

    # define o tempo limite de "atividade" do token
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    data_to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
    


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def auth_user(email: str, password: str, session: Session = Depends(get_session)):
    user = session.scalar({
        select(User).where(
            User.email == email
        )
    })

    if not user:
        return False
    
    elif not verify_password(password, user.password): 
        return False

    return user



def get_current_user(session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(  
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Não foi possível validar as credenciais',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception  
        token_data = TokenData(username=username)

    except jwt.DecodeError:
        raise credentials_exception  

    user = session.scalar(
        select(User).where(User.email == token_data.username)
    )

    if not user:
        raise credentials_exception  

    return user


def get_current_admin(current_user: User = Depends(get_current_user)):
    if current_user.type != "administrator":
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Sem permissões suficientes")
    return current_user