from flask import json, Response


class ValidationException(Exception):
    code: int
    response: Response

    def __init__(
            self,
            code: int,
            api_error_code: int,
            api_error_event: str,
            documentation: str,
            description="Something Went Wrong"
    ):
        self.code = code
        self.response = Response(
            {
                json.dumps({
                    "code": code,
                    "api_error_code": api_error_code,
                    "api_error_event": api_error_event,
                    "documentation": documentation,
                    "description": description,
                }),
            },
            content_type="application/json",
        )

    pass

    def get_response(self) -> Response:
        return self.response
