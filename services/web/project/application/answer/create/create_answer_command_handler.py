from dataclasses import dataclass

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

    def __call__(
        self,
        create_answer_command: CreateAnswerCommand,
    ) -> Answer:
        return self.create_answer_use_case.__call__(
            id_question=create_answer_command.id_question,
            text=create_answer_command.text,
        )
