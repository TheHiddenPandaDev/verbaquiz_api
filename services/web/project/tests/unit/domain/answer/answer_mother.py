from typing import Optional
from faker import Faker

from project.domain.answer.answer import Answer


class AnswerMother:

    @staticmethod
    def create(
            answer_id: int,
            text: str
    ) -> Answer:
        return Answer(
            answer_id=answer_id,
            text=text,
        )

    @staticmethod
    def random(
            answer_id: Optional[int] = None,
            text: Optional[str] = None,
    ) -> Answer:
        fake: Faker = Faker()

        return AnswerMother.create(
            answer_id or fake.random_int(),
            text or fake.pystr(),
        )
