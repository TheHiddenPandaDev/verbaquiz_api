from __future__ import annotations

from datetime import datetime
from typing import Optional

from project import db
from project.utils.datetime_utils import get_local_datetime, readable_datetime

from project.domain.quizz.quizz import Quizz
from project.domain.question.question import Question


class Category(db.Model):
    __tablename__ = 'category'

    category_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(64))
    is_disabled: bool = db.Column(db.Boolean, default=False, nullable=False)

    questions = db.relationship("Question", back_populates="category")

    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
            self,
            category_id: Optional[int],
            name: str,
            is_disabled: Optional[bool],
    ):
        self.category_id = category_id
        self.name = name
        self.is_disabled = is_disabled

    @classmethod
    def create(
            cls,
            category_id: Optional[int],
            name: str,
            is_disabled: Optional[bool],
    ) -> Category:
        return cls(
            category_id,
            name,
            is_disabled,
        )

    def to_json(self) -> dict:
        return {
            "category_id": self.category_id,
            "name": self.name,
            "is_disabled": self.is_disabled,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
