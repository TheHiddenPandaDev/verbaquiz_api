from functools import lru_cache

import typer

from fastapi import status
from fastapi.responses import JSONResponse

from project import app
from project.core.setup import setup_project
from project.domain.answer import answer
from project.domain.answer.answer import Answer
from project.core.settings import Settings
from project.core.database import get_db, engine

setup_project()

cli = typer.Typer()


@lru_cache()
def get_settings():
    return Settings()


@app.exception_handler(Exception)
def handle_error(e):
    if hasattr(e, 'get_response') and hasattr(e, 'code'):
        return e.get_response(), e.code

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": str(e)
        }
    )


@app.on_event("startup")
async def startup():
    database = get_db().__next__()
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    database = get_db().__next__()
    await database.disconnect()


def create_db():

    answer.Base.metadata.drop_all(engine)
    answer.Base.metadata.create_all(engine)

    print("Creating DB")

    database = get_db().__next__()

    database.add(Answer(
        text="Test",
    ))
    database.commit()


if __name__ == "__main__":
    create_db()
