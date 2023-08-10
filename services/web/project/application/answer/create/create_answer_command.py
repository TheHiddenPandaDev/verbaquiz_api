from dataclasses import dataclass


@dataclass
class CreateAnswerCommand:
    id_question: int
    text: str

    def __init__(
        self,
        id_question: int,
        text: str,
    ):
        self.id_question = id_question
        self.text = text
