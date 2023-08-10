from dataclasses import dataclass

from project.api_errors import ApiErrors
from project.documentation_urls import DocumentationUrls
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
        id_question: int,
        text: str,
    ):
        if (
            self.question_finder.__call__(id_question=id_question) is None
        ):
            raise QuestionNotFoundException(
                code=400,
                description=f"id_question: {id_question}. Don't exist in database.",
                api_error_code=ApiErrors.table_answer_unexpected_error['code'],
                api_error_event=ApiErrors.table_answer_unexpected_error['event'],
                documentation=DocumentationUrls.url_create_answer,
            )
        self.answer_creator.__call__(text)
