from typing import Optional
from faker import Faker

from project.domain.question.question import Question


class QuestionMother:

    @staticmethod
    def create(
        question_id: int,
        text: str
    ) -> Question:
        return Question(
            question_id=question_id,
            text=text,
        )

    @staticmethod
    def random(
        question_id: Optional[int] = None,
        text: Optional[str] = None,
    ) -> Question:
        fake: Faker = Faker()

        return QuestionMother.create(
            question_id or fake.random_int(),
            text or fake.pystr(),
        )
