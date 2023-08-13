from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistence.PostgreSQL.quizz.quizz_repository import QuizzRepository
from ..quizz import Quizz


@dataclass
class QuizzFinder:
    quizz_repository: QuizzRepository

    def __init__(
        self,
        quizz_repository: QuizzRepository,
    ):
        self.quizz_repository = quizz_repository

    def __call__(
            self,
            quizz_id: int
    ) -> Optional[Quizz]:
        return self.quizz_repository.get(
            quizz_id
        )
