from flask_api import status
from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

from project.documentation_urls import DocumentationUrls
from project.domain.answer.answer import Answer
from project.container import Container
from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository

blueprint = Blueprint('get_answer_route', __name__)


@blueprint.route("/<id_answer>", methods=["GET"])
@inject
def get_answer(
    id_answer: int,
    repository: AnswerRepository = Provide[Container.answer_repository],
) -> tuple[
    Response, int
]:
    answer: Answer = repository.get(id_answer)

    api_response: dict = {
        "code": status.HTTP_200_OK,
        "api_error_code": None,
        "api_error_event": None,
        "documentation": DocumentationUrls.url_get_answer,
        "description": "OK",
    }

    if answer is None:
        api_response.update({"description": "NOT FOUND"})
        api_response.update({"code": status.HTTP_404_NOT_FOUND})
        api_response.update({"answer": None})
        return jsonify(api_response), status.HTTP_404_NOT_FOUND

    api_response.update({"answer": answer.to_json()})
    return jsonify(api_response), status.HTTP_200_OK
