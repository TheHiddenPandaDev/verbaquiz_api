from dataclasses import dataclass

from project.domain.answer.answer import Answer
from .update_answer_text_command import UpdateAnswerTextCommand
from .update_answer_text_use_case import UpdateAnswerTextUseCase


@dataclass
class UpdateAnswerTextCommandHandler:
    update_answer_text_use_case: UpdateAnswerTextUseCase

    def __init__(
        self,
        update_answer_text_use_case: UpdateAnswerTextUseCase,
    ):
        self.update_answer_text_use_case = update_answer_text_use_case

    def __call__(
        self,
        update_answer_text_command: UpdateAnswerTextCommand,
    ) -> Answer:
        return self.update_answer_text_use_case.__call__(
            id_answer=update_answer_text_command.id_answer,
            text=update_answer_text_command.text,
        )
