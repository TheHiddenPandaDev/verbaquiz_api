from abc import ABC
from typing import Optional

from project.domain.answer.answer import Answer


class ITAnswerRepository(ABC):

    def create(
        self,
        answer: Answer,
    ) -> Answer:
        ...

    def update_text(
        self,
        answer: Answer,
        text: str,
    ) -> Answer:
        ...

    def get_all(self) -> None:
        ...

    def get(self, id_answer: int) -> Optional[Answer]:
        ...
