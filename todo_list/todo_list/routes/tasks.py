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
    
    db_task = Task(title=task.title, description=task.description, status=task.status, user_id=current_user.id)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.get("/me/", status_code=HTTPStatus.OK)
def get_tasks(session: Session = Depends(get_session), 
              current_user: User = Depends(get_current_user)) -> TaskList:
    
    # só pega as tasks do usuário autenticado
    tasks = session.scalars(select(Task).where(
        Task.user_id == current_user.id
    )).all()

    return {"tasks": tasks}


@router.get('/me/{task_id}', status_code=HTTPStatus.OK)
def get_task_by_id(task_id: int, 
                session: Session = Depends(get_session), 
                current_user: User = Depends(get_current_user)) -> TaskPublic:
    
    db_task = session.scalar(
        select(Task).where(Task.id == task_id)
    )
    
    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Tarefa não encontrada.'
        )

    if current_user.id != db_task.user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Sem permissões suficientes'
        )


    return db_task


@router.patch('/me/{task_id}', status_code=HTTPStatus.OK)
def update_task(task_id: int, task: TaskUpdate, 
                session: Session = Depends(get_session), 
                current_user: User = Depends(get_current_user)) -> TaskPublic:
    
    db_task = session.scalar(
        select(Task).where(Task.id == task_id)
    )
    
    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Tarefa não encontrada.'
        )

    if current_user.id != db_task.user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Sem permissões suficientes'
        )

    update_data = task.dict(exclude_unset=True)

    if (update_data):
        stmt = update(Task).where(Task.id == task_id).values(**update_data)

        session.execute(stmt)
        session.commit()
        session.refresh(db_task)

    return db_task


@router.delete('/me/{task_id}', status_code=HTTPStatus.OK)
def delete_task(task_id: int, 
                session: Session = Depends(get_session), 
                current_user: User = Depends(get_current_user)) -> Message:
    
    db_task = session.scalar(
            select(Task).where(Task.id == task_id)
        )
    
    if not db_task:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Tarefa não encontrada.'
        )

    if current_user.id != db_task.user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Sem permissões suficientes'
        )

    session.delete(db_task)
    session.commit()

    return {'message': 'Tarefa deletada com sucesso.'}