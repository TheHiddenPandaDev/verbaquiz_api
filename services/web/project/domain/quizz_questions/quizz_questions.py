from __future__ import annotations

from sqlalchemy import Integer, ForeignKey, Column

from project import db


class QuizzQuestion(db.Model):

    __tablename__ = 'quizz_question'

    quizz_id = Column(Integer, ForeignKey('quizz.quizz_id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('question.question_id'), primary_key=True)

    def __init__(
        self,
        quizz_id: int,
        question_id: int,
    ):
        self.quizz_id = quizz_id
        self.question_id = question_id

    @classmethod
    def create(
        cls,
        quizz_id: int,
        question_id: int,
    ) -> QuizzQuestion:
        return cls(
            quizz_id,
            question_id,
        )
