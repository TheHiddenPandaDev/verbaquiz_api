from flask_api import status
from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

from project.documentation_urls import DocumentationUrls
from project.container import Container
from project.domain.question.question import Question
from project.infrastructure.persistence.PostgreSQL.question.question_repository import QuestionRepository

blueprint = Blueprint('get_question_route', __name__)


@blueprint.route("/<question_id>", methods=["GET"])
@inject
def get_question(
    question_id: int,
    repository: QuestionRepository = Provide[Container.question_repository],
) -> tuple[
    Response, int
]:
    question: Question = repository.get(question_id)

    api_response: dict = {
        "code": status.HTTP_200_OK,
        "api_error_code": None,
        "api_error_event": None,
        "documentation": DocumentationUrls.url_get_answer,
        "description": "OK",
    }

    if question is None:
        api_response.update({"description": "NOT FOUND"})
        api_response.update({"code": status.HTTP_404_NOT_FOUND})
        api_response.update({"answer": None})
        return jsonify(api_response), status.HTTP_404_NOT_FOUND

    api_response.update({"response": question.to_json()})
    return jsonify(api_response), status.HTTP_200_OK
