from abc import ABC
from typing import Optional

from project.domain.quizz.quizz import Quizz


class ITQuizzRepository(ABC):
    def get_all(self) -> None:
        ...

    def get(self, quizz_id: int) -> Optional[Quizz]:
        ...
