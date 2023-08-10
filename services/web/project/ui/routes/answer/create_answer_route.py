from flask import Blueprint, request, json, jsonify
from dependency_injector.wiring import inject, Provide
from flask_api import status
from werkzeug import Response

from project.application.answer.create.create_answer_command import CreateAnswerCommand
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.container import Container
from project.documentation_urls import DocumentationUrls
from project.domain.answer.answer import Answer
from project.infrastructure.validation.validation_exception import ValidationException
from project.infrastructure.validation.validation_rules.create_answer_route_validation_rules import \
    CreateAnswerRouteValidationRules
from project.infrastructure.validation.validator import Validator

blueprint = Blueprint('create_answer_route', __name__)


@blueprint.route("/create", methods=["POST"])
@inject
def create_answer(
        create_answer_command_handler: CreateAnswerCommandHandler = Provide[Container.create_answer_command_handler],
) -> [Response, int]:
    post_request: dict = request.get_json()

    try:
        Validator.validate(
            json_to_validate=post_request,
            json_validation_rules=CreateAnswerRouteValidationRules
        )
    except ValidationException as e:
        return jsonify(
            {
                "code": CreateAnswerRouteValidationRules.http_error_code,
                "api_error_code": CreateAnswerRouteValidationRules.api_error_code,
                "api_error_event": CreateAnswerRouteValidationRules.api_error_event,
                "documentation": CreateAnswerRouteValidationRules.documentation,
            }
        ), CreateAnswerRouteValidationRules.http_error_code

    create_answer_command = CreateAnswerCommand(
        id_question=post_request['id_question'],
        text=post_request['text'],
    )

    answer: Answer = create_answer_command_handler.__call__(create_answer_command)

    return jsonify(
        {
            "code": status.HTTP_201_CREATED,
            "api_error_code": None,
            "api_error_event": None,
            "documentation": DocumentationUrls.url_create_answer,
            "description": "OK",
            "answer": answer.to_json(),
        }
    ), status.HTTP_201_CREATED,
