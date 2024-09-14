from fastapi import FastAPI
from todo_list.routes.users import router as usersRoute
from todo_list.routes.auth import router as authRoute
from todo_list.routes.tasks import router as tasksRoute

app = FastAPI()

app.include_router(usersRoute)
app.include_router(authRoute)
app.include_router(tasksRoute)