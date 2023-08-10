from __future__ import annotations

import pytz as pytz
from datetime import datetime
from typing import Optional


from project import db


class Answer(db.Model):
    dt = datetime.now(tz=pytz.timezone('Europe/Madrid'))

    answer_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=dt)
    updated_at: datetime = db.Column(db.DateTime, default=dt, onupdate=dt)

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
            "created_at": self.created_at.strftime("%d-%m-%Y %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%d-%m-%Y %H:%M:%S"),
        }
