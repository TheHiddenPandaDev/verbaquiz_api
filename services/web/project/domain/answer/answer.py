from sqlalchemy import Column, Integer, String

from project.core.database import Base


class Answer(Base):
    __tablename__ = "answers"

    answer_id: int = Column(Integer, primary_key=True, index=True)
    text: str = Column(String, unique=True)

    def json(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "text": self.text,
        }
