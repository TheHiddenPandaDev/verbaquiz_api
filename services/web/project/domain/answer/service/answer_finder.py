from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository
from ..answer import Answer


@dataclass
class AnswerFinder:
    answer_repository: AnswerRepository

    def __init__(
            self,
            answer_repository: AnswerRepository,
    ):
        self.answer_repository = answer_repository

    def __call__(
            self,
            answer_id: int
    ) -> Optional[Answer]:
        return self.answer_repository.get(
            answer_id
        )
