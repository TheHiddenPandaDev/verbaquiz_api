from dataclasses import dataclass
from typing import Optional

from project.domain.answer.repository.answer_repository import ITAnswerRepository
from project.domain.answer.answer import Answer


@dataclass
class AnswerRepository(ITAnswerRepository):

    def get_all(self) -> list[Answer]:
        return Answer.query.all()

    def get(self, id_answer: int) -> Optional[Answer]:
        return Answer.query.get(id_answer)

    def create(self, answer: Answer) -> Optional[int]:
        # Answer.query.create(answer)
        return 1
