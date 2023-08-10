from flask_api import status

from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
from project.infrastructure.validation.abstract_validation_rules import AbstractValidationRules


class CreateAnswerRouteValidationRules(AbstractValidationRules):

    schema: dict = {
        "type": "object",
        "properties": {
            "id_question": {
                "type": "number",
                "minimum": 0,
            },
            "text": {
                "type": "string",
            },
        },
        "required": [
            "id_question",
            "text"
         ],
    }
    http_error_code: int = status.HTTP_400_BAD_REQUEST
    api_error_code: int = ApiErrors.table_answer_unexpected_error['code']
    api_error_event: str = ApiErrors.table_answer_unexpected_error['event']
    documentation: str = DocumentationUrls.url_create_answer
