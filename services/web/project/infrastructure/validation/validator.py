from typing import Type

from jsonschema.exceptions import ValidationError, SchemaError
from jsonschema.validators import validate

from project.infrastructure.validation.abstract_validation_rules import AbstractValidationRules
from project.infrastructure.validation.validation_exception import ValidationException


class Validator(object):

    @staticmethod
    def validate(
        json_to_validate: dict,
        json_validation_rules: Type[AbstractValidationRules],
    ) -> None:
        try:
            validate(
                instance=json_to_validate,
                schema=json_validation_rules.schema
            )
        except (SchemaError, ValidationError) as e:
            raise ValidationException(
                code=json_validation_rules.http_error_code,
                description=e.message,
                api_error_code=json_validation_rules.api_error_code,
                api_error_event=json_validation_rules.api_error_event,
                documentation=json_validation_rules.documentation,
            )
