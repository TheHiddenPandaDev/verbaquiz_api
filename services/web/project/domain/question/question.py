from __future__ import annotations

from typing import Optional

from project import db


class Question(db.Model):
    question_id: int = db.Column(db.Integer, primary_key=True)
    text: str = db.Column(db.String(64), unique=True)
    # created_at
    # updated_at

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

    def json(self) -> dict:
        return {
            "question_id": self.question_id,
            "text": self.text,
        }
