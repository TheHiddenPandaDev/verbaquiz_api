from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistence.PostgreSQL.question.question_repository import QuestionRepository
from ..question import Question


@dataclass
class QuestionFinder:
    question_repository: QuestionRepository

    def __init__(
        self,
        question_repository: QuestionRepository,
    ):
        self.question_repository = question_repository

    def __call__(
            self,
            question_id: int
    ) -> Optional[Question]:
        return self.question_repository.get(
            question_id
        )
