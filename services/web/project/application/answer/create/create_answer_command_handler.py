from dataclasses import dataclass
from typing import Optional

from project.domain.answer.answer import Answer
from .create_answer_command import CreateAnswerCommand
from .create_answer_use_case import CreateAnswerUseCase


@dataclass
class CreateAnswerCommandHandler:
    create_answer_use_case: CreateAnswerUseCase

    def __init__(
        self,
        create_answer_use_case: CreateAnswerUseCase,
    ):
        self.create_answer_use_case = create_answer_use_case

    def execute(
        self,
        create_user_command: CreateAnswerCommand
    ) -> Optional[Answer]:
        return self.create_answer_use_case.execute(
            create_user_command.text,
        )
