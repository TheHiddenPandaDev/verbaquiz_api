from dataclasses import dataclass
from typing import Optional

from fastapi import Depends

from project.domain.answer.answer import Answer
from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository


@dataclass
class AnswerCreator:
    answer_repository: AnswerRepository

    def __init__(
            self,
            answer_repository: AnswerRepository = Depends(AnswerRepository)
    ):
        self.answer_repository = answer_repository

    def execute(
        self,
        text: str
    ) -> Optional[Answer]:
        answer = Answer(
            text=text,
        )
        return self.answer_repository.create(answer)
