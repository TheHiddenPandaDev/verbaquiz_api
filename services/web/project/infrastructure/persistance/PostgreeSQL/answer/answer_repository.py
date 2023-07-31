from dataclasses import dataclass
from typing import Optional

from project.domain.answer.repository.answer_repository import ITAnswerRepository
from project.domain.answer.answer import Answer
from project.core.database import get_db


@dataclass
class AnswerRepository(ITAnswerRepository):

    def get_all(self) -> list[Answer]:
        return Answer.query.all()

    def get(self, answer_id: int) -> Optional[Answer]:
        db = get_db().__next__()

        return db.query(Answer).filter(Answer.answer_id == answer_id).first()

    def create(self, answer: Answer) -> Optional[int]:
        # Answer.query.create(answer)
        return 1