from sqlalchemy import Column, Integer, String

from project.core.database import Base


class Answer(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=True)

    """
    def json() -> dict:
        return {
            "answer_id": answer_id,
            "text": self.text,
        }
    """