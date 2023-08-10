from dataclasses import dataclass

from project.domain.answer.answer import Answer
from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository


@dataclass
class AnswerTextUpdater:
    answer_repository: AnswerRepository

    def __init__(
        self,
        answer_repository: AnswerRepository,
    ):
        self.answer_repository = answer_repository

    def __call__(
        self,
        answer: Answer,
        text: str
    ) -> Answer:
        return self.answer_repository.update_text(
            answer=answer,
            text=text,
        )
