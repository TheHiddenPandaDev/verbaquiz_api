from dataclasses import dataclass
from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from project.domain.answer.repository.answer_repository import ITAnswerRepository
from project.domain.answer.answer import Answer
from project.core.database import get_db


@dataclass
class AnswerRepository(ITAnswerRepository):
    db: Session

    def __init__(
            self,
            db: Session = Depends(get_db)
    ):
        self.db = db

    def get_all(self) -> list[Answer]:
        return Answer.query.all()

    def get(self, answer_id: int) -> Optional[Answer]:
        return self.db.query(Answer).filter(Answer.answer_id == answer_id).first()

    def create(self, answer: Answer) -> Optional[Answer]:
        self.db.add(answer)
        self.db.commit()
        self.db.refresh(answer)
        return answer
