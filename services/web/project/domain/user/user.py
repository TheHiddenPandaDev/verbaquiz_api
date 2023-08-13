from __future__ import annotations

from datetime import datetime
from typing import Optional

from project import db, Base
from project.utils.datetime_utils import get_local_datetime, readable_datetime


class User(db.Model):

    __tablename__ = 'user'

    user_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(64))
    is_disabled: bool = db.Column(db.Boolean, default=False, nullable=False)

    quizzes = db.relationship("Quizz", back_populates="user")

    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(
        self,
        user_id: Optional[int],
        name: str,
        is_disabled: Optional[bool],
    ):
        self.user_id = user_id
        self.name = name
        self.is_disabled = is_disabled

    @classmethod
    def create(
        cls,
        user_id: Optional[int],
        name: str,
        is_disabled: Optional[bool],
    ) -> User:
        return cls(
            user_id,
            name,
            is_disabled,
        )

    def to_json(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "is_disabled": self.is_disabled,
            "created_at": readable_datetime(get_local_datetime(self.created_at)),
            "updated_at": readable_datetime(get_local_datetime(self.updated_at)),
        }
