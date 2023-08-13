from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from project import db
from project.utils.datetime_utils import get_local_datetime, readable_datetime


class Quizz(db.Model):

    quizz_id: int = db.Column(db.Integer, primary_key=True)

    questions = relationship("Question", secondary="quizz_question", back_populates="quizzes")

    category_id = mapped_column(Integer, ForeignKey('category.category_id'))
    category = relationship("Quizz", back_populates="quizzes", foreign_keys=[category_id])

    user_id = mapped_column(Integer, ForeignKey('user.user_id'))
    user = relationship("User", back_populates="quizzes", foreign_keys=[user_id])

    status: str = db.Column(db.String(64))

    quizz_duration_in_seconds: int = db.Column(db.Integer)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        quizz_id: Optional[int],
        category_id: int,
        user_id: int,
        status: str,
        quizz_duration_in_seconds: int,
    ):
        self.quizz_id = quizz_id
        self.category_id = category_id
        self.user_id = user_id
        self.status = status
        self.quizz_duration_in_seconds = quizz_duration_in_seconds

    @classmethod
    def create(
        cls,
        quizz_id: int,
        category_id: int,
        user_id: int,
        status: str,
        quizz_duration_in_seconds: int,
    ) -> Quizz:
        return cls(
            quizz_id,
            category_id,
            user_id,
            status,
            quizz_duration_in_seconds,
        )

    def to_json(self) -> dict:
        questions: list = []

        for question in self.questions:
            questions.append(question.to_json())

        return {
            "quizz_id": self.quizz_id,
            "category_id": self.category_id,
            "user_id": self.user_id,
            "status": self.status,
            "quizz_duration_in_seconds": self.quizz_duration_in_seconds,
            "questions": questions,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
