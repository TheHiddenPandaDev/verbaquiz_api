from __future__ import annotations

from datetime import datetime
from typing import Optional

from project import db
from project.utils.datetime_utils import get_local_datetime, readable_datetime


class Question(db.Model):
    question_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        question_id: Optional[int],
        text: str,
    ):
        self.question_id = question_id
        self.text = text

    @classmethod
    def create(
        cls,
        question_id: int,
        text: str,
    ) -> Question:
        return cls(
            question_id,
            text,
        )

    def to_json(self) -> dict:
        return {
            "question_id": self.question_id,
            "text": self.text,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
