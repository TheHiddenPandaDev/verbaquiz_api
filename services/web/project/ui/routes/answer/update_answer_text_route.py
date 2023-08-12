from flask import Blueprint, request, json, jsonify
from dependency_injector.wiring import inject, Provide
from flask_api import status
from werkzeug import Response

from project.application.answer.update_answer_text.update_answer_text_command import UpdateAnswerTextCommand
from project.application.answer.update_answer_text.update_answer_text_command_handler import \
    UpdateAnswerTextCommandHandler
from project.container import Container
from project.documentation_urls import DocumentationUrls
from project.domain.answer.answer import Answer
from project.infrastructure.validation.validation_exception import ValidationException
from project.infrastructure.validation.validation_rules.update_answer_text_route_validation_rules import \
    UpdateAnswerTextRouteValidationRules
from project.infrastructure.validation.validator import Validator

blueprint = Blueprint('update_answer_text_route', __name__)


@blueprint.route("<answer_id>/update/", methods=["PUT"])
@inject
def update_answer(
    answer_id: int,
    update_answer_text_command_handler: UpdateAnswerTextCommandHandler = Provide[Container.update_answer_text_command_handler],
) -> [Response, int]:

    put_request: dict = request.get_json()

    try:
        Validator.validate(
            json_to_validate=put_request,
            json_validation_rules=UpdateAnswerTextRouteValidationRules
        )
    except ValidationException as e:
        return jsonify(
            {
                "code": UpdateAnswerTextRouteValidationRules.http_error_code,
                "api_error_code": UpdateAnswerTextRouteValidationRules.api_error_code,
                "api_error_event": UpdateAnswerTextRouteValidationRules.api_error_event,
                "documentation": UpdateAnswerTextRouteValidationRules.documentation,
            }
        ), UpdateAnswerTextRouteValidationRules.http_error_code

    update_answer_text_command = UpdateAnswerTextCommand(
        answer_id=answer_id,
        text=put_request['text'],
    )

    answer: Answer = update_answer_text_command_handler.__call__(update_answer_text_command)

    return jsonify(
        {
            "code": status.HTTP_201_CREATED,
            "api_error_code": None,
            "api_error_event": None,
            "documentation": DocumentationUrls.url_create_answer,
            "description": "OK",
            "response": answer.to_json(),
        }
    ), status.HTTP_201_CREATED,
