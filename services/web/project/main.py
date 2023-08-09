from fastapi import FastAPI

from project.ui.routes.answer.get_answer_route import get_answer_route
from project.ui.routes.answer.create_answer_route import create_answer_route

app = FastAPI()

app.include_router(get_answer_route)
app.include_router(create_answer_route)