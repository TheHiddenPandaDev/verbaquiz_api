from sqlalchemy import Column, Integer, String

from project.core.database import Base


class Answer(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=False)

    def to_json(self) -> dict:
        return {
            "answer_id": self.answer_id,
            "text": self.text,
        }
