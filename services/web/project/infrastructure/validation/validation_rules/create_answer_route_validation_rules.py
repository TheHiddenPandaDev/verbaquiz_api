from fastapi import status

from project.core.api_errors import ApiErrors
from project.core.documentation_urls import DocumentationUrls
from project.infrastructure.validation.abstract_validation_rules import AbstractValidationRules


class CreateAnswerRouteValidationRules(AbstractValidationRules):

    schema: dict = {
        "type": "object",
        "properties": {
            "text": {"type": "string"},
        },
        "required": ["text"],
    }
    http_error_code: int = status.HTTP_400_BAD_REQUEST
    api_error_code: int = ApiErrors.table_answer_unexpected_error['code']
    api_error_event: str = ApiErrors.table_answer_unexpected_error['event']
    documentation: str = DocumentationUrls.url_create_answer
