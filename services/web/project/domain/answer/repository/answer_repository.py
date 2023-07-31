from abc import ABC
from typing import Optional

from project.domain.answer.answer import Answer


class ITAnswerRepository(ABC):
    def get_all(self) -> None:
        ...

    def get(self, answer_id: int) -> Optional[Answer]:
        ...

    def create(self, answer: Answer) -> Optional[int]:
        ...