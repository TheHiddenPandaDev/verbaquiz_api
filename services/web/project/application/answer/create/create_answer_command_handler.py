from dataclasses import dataclass

from .create_answer_command import CreateAnswerCommand
from .create_answer_use_case import CreateAnswerUseCase


@dataclass
class CreateAnswerCommandHandler:
    create_user_use_case: CreateAnswerUseCase

    def __init__(
        self,
        create_user_use_case: CreateAnswerUseCase,
    ):
        self.create_user_use_case = create_user_use_case


    def __call__(
        self,
        create_user_command: CreateAnswerCommand
    ):
        self.create_user_use_case.__call__(
            create_user_command.text,
        )