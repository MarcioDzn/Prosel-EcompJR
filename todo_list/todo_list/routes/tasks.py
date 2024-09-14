from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException, Query
from todo_list.models.models import Task, User

from sqlalchemy import select, update
from sqlalchemy.orm import Session
from todo_list.configs.database import get_session

from todo_list.schemas.task import TaskCreate, TaskPublic, TaskList, TaskUpdate
from todo_list.schemas.message import Message

from todo_list.security import *

router = APIRouter(prefix="/tasks", tags=["task"])

@router.post("/", status_code=HTTPStatus.CREATED)
def create_task(task: TaskCreate, 
                session: Session = Depends(get_session), 
                current_user: User = Depends(get_current_user)) -> TaskPublic:
    
    user_id = current_user.id

    # verifica se já existe um usuário com o id
    db_user = session.scalar(
        select(User).where(
            user_id == User.id
        )
    )

    if (not db_user):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefa não encontrada")
    
    db_task = Task(title=task.title, description=task.description, status=task.status, user_id=user_id)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task

