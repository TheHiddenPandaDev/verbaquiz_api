from dataclasses import dataclass


@dataclass
class CreateAnswerCommand:
    question_id: int
    text: str

    def __init__(
        self,
        question_id: int,
        text: str,
    ):
        self.question_id = question_id
        self.text = text
