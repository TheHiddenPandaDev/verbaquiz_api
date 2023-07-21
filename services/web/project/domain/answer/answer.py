from __future__ import annotations

from project import db


class Answer(db.Model):
    answer_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64), unique=True)

    def __init__(
            self,
            answer_id: int,
            text: str,
    ):
        self.answer_id = answer_id
        self.text = text

    @classmethod
    def create(cls,
               answer_id: int,
               text: str,
               ) -> Answer:
        return cls(
            answer_id,
            text,
        )

    def json(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "text": self.text,
        }
