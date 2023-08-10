from abc import ABC
from typing import Optional

from project.domain.question.question import Question


class ITQuestionRepository(ABC):
    def get_all(self) -> None:
        ...

    def get(self, id_question: int) -> Optional[Question]:
        ...
