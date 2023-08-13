from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from project import db
from project.utils.datetime_utils import get_local_datetime, readable_datetime


class Question(db.Model):
    __tablename__ = 'question'

    question_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))

    quizzes = relationship("Quizz", secondary="quizz_question", back_populates="questions")

    answers = db.relationship("Answer", back_populates="question", primaryjoin="Answer.question_id==Question.question_id")

    category_id = mapped_column(Integer, ForeignKey('category.category_id'))
    category = relationship("Category", back_populates="questions", foreign_keys=[category_id])

    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        question_id: Optional[int],
        category_id: int,
        text: str,
    ):
        self.question_id = question_id
        self.category_id = category_id
        self.text = text

    @classmethod
    def create(
        cls,
        question_id: Optional[int],
        category_id: int,
        text: str,
    ) -> Question:
        return cls(
            question_id,
            category_id,
            text,
        )

    def to_json(self) -> dict:

        answers: list = []
        correct_answer: Optional[dict] = None

        for answer in self.answers:
            answers.append(answer.to_json())

            if answer.is_correct:
                correct_answer = answer.to_json()

        return {
            "question_id": self.question_id,
            "category_id": self.category_id,
            "text": self.text,
            "correct_answer": correct_answer,
            "answers": answers,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
