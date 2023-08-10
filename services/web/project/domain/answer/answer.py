from __future__ import annotations

from datetime import datetime
from typing import Optional


from project import db
from project.utils.datetime_utils import get_local_date_time


class Answer(db.Model):
    answer_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        answer_id: Optional[int],
        text: str,
    ):
        self.answer_id = answer_id
        self.text = text

    @classmethod
    def create(
        cls,
        answer_id: Optional[int],
        text: str,
    ) -> Answer:
        return cls(
            answer_id,
            text,
        )

    def to_json(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "text": self.text,
            "created_at": self.created_at.get_local_date_time().readable(),
            "updated_at": self.updated_at.get_local_date_time().readable(),
        }
