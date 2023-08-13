from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from project import db, Base
from project.utils.datetime_utils import get_local_datetime, readable_datetime


class Answer(db.Model):

    __tablename__ = 'answer'

    answer_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))
    is_correct: bool = db.Column(db.Boolean, default=False, nullable=False)

    # Answers
    question_id = mapped_column(Integer, ForeignKey('question.question_id'))
    question = relationship("Question", back_populates="answers", foreign_keys=[question_id])

    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        answer_id: Optional[int],
        text: str,
        is_correct: bool,
        question_id: int,
    ):
        self.answer_id = answer_id
        self.text = text
        self.is_correct = is_correct
        self.question_id = question_id

    @classmethod
    def create(
        cls,
        answer_id: Optional[int],
        text: str,
        is_correct: bool,
        question_id: int,
    ) -> Answer:
        return cls(
            answer_id,
            text,
            is_correct,
            question_id,
        )

    def to_json(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "text": self.text,
            "is_correct": self.is_correct,
            "question_id": self.question_id,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
