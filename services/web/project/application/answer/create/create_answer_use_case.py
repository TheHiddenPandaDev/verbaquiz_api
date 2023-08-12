from dataclasses import dataclass

from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
from project.domain.answer.answer import Answer
from project.domain.question.exception.question_not_found_exception import QuestionNotFoundException
from project.domain.question.service.question_finder import QuestionFinder

from .answer_creator import AnswerCreator


@dataclass
class CreateAnswerUseCase:
    answer_creator: AnswerCreator
    question_finder: QuestionFinder

    def __init__(
        self,
        answer_creator: AnswerCreator,
        question_finder: QuestionFinder,
    ):
        self.answer_creator = answer_creator
        self.question_finder = question_finder

    def __call__(
        self,
        question_id: int,
        text: str,
    ) -> Answer:
        if (
            self.question_finder.__call__(question_id=question_id) is None
        ):
            raise QuestionNotFoundException(
                code=400,
                description=f"question_id: {question_id}. Don't exist in database.",
                api_error_code=ApiErrors.table_answer_unexpected_error['code'],
                api_error_event=ApiErrors.table_answer_unexpected_error['event'],
                documentation=DocumentationUrls.url_create_answer,
            )
        return self.answer_creator.__call__(text)
