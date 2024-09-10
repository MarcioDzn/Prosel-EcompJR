from datetime import timedelta, datetime, timezone

import jwt
from jwt.exceptions import InvalidTokenError

from passlib.context import CryptContext
from sqlalchemy import select
from todo_list.models.models import User

SECRET_KEY="9279843e857e59924bffb1f77343f936256e4951ebba20a102d2998a5eb316b3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


def hash_pasword(password):
    return pwd_context.hash(password)


def auth_user(session, email: str, password: str):
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
