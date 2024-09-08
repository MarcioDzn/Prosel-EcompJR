from fastapi import FastAPI
from todo_list.routes.users import router as usersRoute

app = FastAPI()

app.include_router(usersRoute)