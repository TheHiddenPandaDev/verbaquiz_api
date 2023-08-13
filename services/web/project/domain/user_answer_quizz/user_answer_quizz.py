from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey, Column

from project import db, Base
from project.utils.datetime_utils import readable_datetime, get_local_datetime


class UserAnswers(db.Model):

    __tablename__ = 'user_answers'

    quizz_id: int = Column(Integer, ForeignKey('quizz.quizz_id'), primary_key=True)
    user_id: int = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    question_id: int = Column(Integer, ForeignKey('question.question_id'), primary_key=True)

    selected_answer_id: int = Column(Integer, ForeignKey('answer.answer_id'), nullable=True)
    correct_answer_id: int = Column(Integer, ForeignKey('answer.answer_id'), nullable=False)

    status: str = db.Column(db.String(64))

    started_at: datetime = db.Column(db.DateTime, nullable=True)
    finished_at: datetime = db.Column(db.DateTime, nullable=True)

    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        quizz_id: int,
        user_id: int,
        question_id: int,
        selected_answer_id: int,
        correct_answer_id: Optional[int],
        status: str,
        started_at: Optional[datetime],
        finished_at: Optional[datetime],
    ):
        self.quizz_id = quizz_id
        self.user_id = user_id
        self.question_id = question_id
        self.selected_answer_id = selected_answer_id
        self.correct_answer_id = correct_answer_id
        self.status = status
        self.started_at = started_at
        self.finished_at = finished_at

    @classmethod
    def create(
        cls,
        quizz_id: int,
        user_id: int,
        question_id: int,
        selected_answer_id: int,
        correct_answer_id: Optional[int],
        status: str,
        started_at: Optional[datetime],
        finished_at: Optional[datetime],
    ) -> UserAnswers:
        return cls(
            quizz_id,
            user_id,
            question_id,
            selected_answer_id,
            correct_answer_id,
            status,
            started_at,
            finished_at,
        )

    def to_json(self) -> dict:
        return {
            "quizz_id": self.quizz_id,
            "user_id": self.user_id,
            "question_id": self.question_id,
            "selected_answer_id": self.selected_answer_id,
            "correct_answer_id": self.correct_answer_id,
            "status": self.status,
            "started_at": readable_datetime(get_local_datetime(self.started_at)),
            "finished_at": readable_datetime(get_local_datetime(self.finished_at)),
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
