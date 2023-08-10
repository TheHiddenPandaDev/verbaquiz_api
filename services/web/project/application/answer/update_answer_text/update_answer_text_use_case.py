from dataclasses import dataclass
from typing import Optional

from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
from project.domain.answer.answer import Answer
from project.domain.answer.service.answer_finder import AnswerFinder
from project.domain.answer.exception.answer_not_found_exception import AnswerNotFoundException

from .answer_text_updater import AnswerTextUpdater


@dataclass
class UpdateAnswerTextUseCase:
    answer_text_updater: AnswerTextUpdater
    answer_finder: AnswerFinder

    def __init__(
        self,
        answer_text_updater: AnswerTextUpdater,
        answer_finder: AnswerFinder,
    ):
        self.answer_text_updater = answer_text_updater
        self.answer_finder = answer_finder

    def __call__(
        self,
        id_answer: int,
        text: str,
    ) -> Answer:
        answer: Optional[Answer] = self.answer_finder.__call__(id_answer=id_answer)

        if answer is None:
            raise AnswerNotFoundException(
                code=400,
                description=f"id_answer: {id_answer}. Don't exist in database.",
                api_error_code=ApiErrors.table_answer_unexpected_error['code'],
                api_error_event=ApiErrors.table_answer_unexpected_error['event'],
                documentation=DocumentationUrls.url_create_answer,
            )
        return self.answer_text_updater.__call__(
            answer=answer,
            text=text,
        )
