from __future__ import annotations

from typing import Optional

from project import db


class Answer(db.Model):
    answer_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64))
    # created_at
    # updated_at

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
        answer_id: int,
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
        }
