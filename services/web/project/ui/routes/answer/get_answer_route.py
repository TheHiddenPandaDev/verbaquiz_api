from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder

from dependency_injector.wiring import inject

from project.domain.answer.answer import Answer
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository

router = APIRouter()


@router.get(
    "/users/{answer_id}",
    tags=["answers"],
    status_code=200,
)
@inject
def get_answer(
        answer_id: int,
        repository: AnswerRepository = Depends(AnswerRepository),
) -> tuple[
    str, int
]:
    answer: Answer = repository.get(answer_id)

    if answer is None:
        return 'No found', status.HTTP_200_OK

    return jsonable_encoder(answer.text), status.HTTP_200_OK
