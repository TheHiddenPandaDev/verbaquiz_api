from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder

from project.domain.answer.answer import Answer
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository

get_answer_route = APIRouter()


@get_answer_route.get(
    "/answers/{answer_id}",
    tags=["answers"],
    status_code=200,
)
def get_answer(
        answer_id: int,
        repository: AnswerRepository = Depends(AnswerRepository),
) -> dict:
    answer: Answer = repository.get(answer_id)

    if answer is None:
        return jsonable_encoder("No found")

    return answer.to_json()
