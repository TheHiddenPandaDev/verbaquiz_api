from flask import Blueprint, jsonify, Response
from dependency_injector.wiring import inject, Provide

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

    if answer is None:
        return jsonify([]), 200

    return jsonify(answer.json()), 200
