from passlib.context import CryptContext
from sqlalchemy import select
from todo_list.models.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
