from dataclasses import dataclass
from typing import Optional

from project.domain.answer.answer import Answer
from .answer_creator import AnswerCreator


@dataclass
class CreateAnswerUseCase:
    answer_creator: AnswerCreator

    def __init__(
            self,
            answer_creator: AnswerCreator,
    ):
        self.answer_creator = answer_creator

    def execute(
            self,
            text: str
    ) -> Optional[Answer]:
        return self.answer_creator.execute(text)
