from dataclasses import dataclass
from typing import Optional

from project.domain.question.repository.question_repository import ITQuestionRepository
from project.domain.question.question import Question


@dataclass
class QuestionRepository(ITQuestionRepository):
    def get_all(self) -> list[Question]:
        return Question.query.all()

    def get(self, id_question: int) -> Optional[Question]:
        return Question.query.get(id_question)
