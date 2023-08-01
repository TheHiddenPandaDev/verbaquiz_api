from typing import Optional

from fastapi import APIRouter, status, Depends, Response

from project.core.documentation_urls import DocumentationUrls
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
    response: Response,
    repository: AnswerRepository = Depends(AnswerRepository),
):
    answer: Optional[Answer] = repository.get(answer_id)

    api_response: dict = {
        "code": status.HTTP_200_OK,
        "api_error_code": None,
        "api_error_event": None,
        "documentation": DocumentationUrls.url_get_answer,
        "description": "OK",
    }

    if answer is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        api_response.update({"description": "NOT FOUND"})
        api_response.update({"code": status.HTTP_404_NOT_FOUND})
        api_response.update({"answer": None})
        return api_response

    api_response.update({"answer": answer.to_json()})
    return api_response
