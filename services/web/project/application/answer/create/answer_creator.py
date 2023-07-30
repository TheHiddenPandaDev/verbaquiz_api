from dataclasses import dataclass

from project.domain.answer.answer import Answer
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository


@dataclass
class AnswerCreator:
    answer_repository: AnswerRepository

    def __init__(
            self,
            answer_repository: AnswerRepository,
    ):
        self.answer_repository = answer_repository

    def __call__(
            self,
            text: str
    ):
        answer = Answer(
            text=text,
        )
        self.answer_repository.create(answer)
