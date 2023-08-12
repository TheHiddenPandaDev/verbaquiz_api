from dataclasses import dataclass


@dataclass
class UpdateAnswerTextCommand:
    answer_id: int
    text: str

    def __init__(
        self,
        answer_id: int,
        text: str,
    ):
        self.answer_id = answer_id
        self.text = text
