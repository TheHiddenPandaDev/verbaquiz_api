from fastapi import FastAPI

from project.core.settings import Settings
from project.ui.routes.answer.get_answer_route import router

settings = Settings()
app = FastAPI()

app.include_router(router)
