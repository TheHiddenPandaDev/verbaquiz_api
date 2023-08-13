from dataclasses import dataclass
from typing import Optional

from project.domain.quizz.repository.quizz_repository import ITQuizzRepository
from project.domain.quizz.quizz import Quizz


@dataclass
class QuizzRepository(ITQuizzRepository):
    def get_all(self) -> list[Quizz]:
        return Quizz.query.all()

    def get(self, quizz_id: int) -> Optional[Quizz]:
        return Quizz.query.get(quizz_id)
