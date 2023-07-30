from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from dependency_injector.wiring import inject, Provide

from project.domain.answer.answer import Answer
from project.core.container_config import Container
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository

router = APIRouter()


@router.get(
    "/users/{id_answer}",
    tags=["answers"],
    status_code=200,
)
@inject
def get_answer(
        id_answer: int,
        repository: AnswerRepository = Provide[Container.answer_repository],
) -> tuple[
    str, int
]:
    answer: Answer = repository.get(id_answer)

    if answer is None:
        return jsonable_encoder([]), status.HTTP_200_OK

    return jsonable_encoder(answer.json()), status.HTTP_200_OK
