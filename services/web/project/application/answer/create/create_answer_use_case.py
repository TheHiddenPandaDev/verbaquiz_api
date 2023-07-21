from dataclasses import dataclass

from .answer_creator import UserCreator


@dataclass
class CreateUserUseCase:
    answer_creator: UserCreator

    def __init__(
            self,
            answer_creator: UserCreator,
    ):
        self.answer_creator = answer_creator

    def __call__(
            self,
            text: str
    ):
        self.answer_creator.__call__(text)
