from dataclasses import dataclass


@dataclass
class UpdateAnswerTextCommand:
    id_answer: int
    text: str

    def __init__(
        self,
        id_answer: int,
        text: str,
    ):
        self.id_answer = id_answer
        self.text = text
