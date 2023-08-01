from fastapi import APIRouter, Depends, status, Request, Response

from project.core.documentation_urls import DocumentationUrls
from project.application.answer.create.answer_creator import AnswerCreator
from project.application.answer.create.create_answer_command import CreateAnswerCommand
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.application.answer.create.create_answer_use_case import CreateAnswerUseCase
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository
from project.infrastructure.validation.validation_exception import ValidationException
from project.infrastructure.validation.validation_rules.answers.create_answer_route_validation_rules import \
    CreateAnswerRouteValidationRules
from project.infrastructure.validation.validator import Validator

create_answer_route = APIRouter()


@create_answer_route.post(
    "/answers/create",
    tags=["answers"],
    status_code=201,
)
async def create_answer(
        request: Request,
        response: Response,
        repository: AnswerRepository = Depends(AnswerRepository),
):
    post_request: dict = await request.json()

    try:
        # noinspection PyTypeChecker
        Validator.validate(
            json_to_validate=post_request,
            json_validation_rules=CreateAnswerRouteValidationRules
        )
    except ValidationException as e:
        response.status_code = CreateAnswerRouteValidationRules.http_error_code
        return {
            "code": CreateAnswerRouteValidationRules.http_error_code,
            "api_error_code": CreateAnswerRouteValidationRules.api_error_code,
            "api_error_event": CreateAnswerRouteValidationRules.api_error_event,
            "documentation": CreateAnswerRouteValidationRules.documentation,
        },

    answer_creator = AnswerCreator(answer_repository=repository)

    create_answer_use_case = CreateAnswerUseCase(answer_creator=answer_creator)

    create_answer_command = CreateAnswerCommand(
        text=post_request['text'],
    )

    create_answer_command_handler = CreateAnswerCommandHandler(create_answer_use_case=create_answer_use_case)

    answer = create_answer_command_handler.execute(create_answer_command)

    return {
        "code": status.HTTP_201_CREATED,
        "api_error_code": None,
        "api_error_event": None,
        "documentation": DocumentationUrls.url_create_answer,
        "description": "OK",
        "answer": answer.to_json()
    }
