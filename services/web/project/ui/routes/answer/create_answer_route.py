from flask import Blueprint, request, json
from dependency_injector.wiring import inject, Provide
from werkzeug import Response

from project.application.answer.create.create_answer_command import CreateAnswerCommand
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.container import Container
from project.documentation_urls import DocumentationUrls
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

    Validator.validate(
        json_to_validate=post_request,
        json_validation_rules=CreateAnswerRouteValidationRules
    )

    create_answer_command = CreateAnswerCommand(
        id_question=post_request['id_question'],
        text=post_request['text'],
    )

    create_answer_command_handler.__call__(create_answer_command)

    return Response(
        {
            json.dumps({
                "code": 201,
                "api_error_code": None,
                "api_error_event": None,
                "documentation": DocumentationUrls.url_create_answer,
                "description": "OK",
            }),
        },
        content_type="application/json",
    ), 201
