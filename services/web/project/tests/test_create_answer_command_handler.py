import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from unittest.mock import Mock

from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository
from project.core.database import Base
from project.core.settings import Settings

SQLALCHEMY_DATABASE_URL = "sqlite://"

Settings.DATABASE_URL = SQLALCHEMY_DATABASE_URL

engine = create_engine(
    'SQLALCHEMY_DATABASE_URL',
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


class CreateAnswerCommandHandlerTest(unittest.TestCase):
    mock_answer_repository = AnswerRepository(TestingSessionLocal())

    def test_create_ok(
            self,
    ):
        assert self.mock_answer_repository is AnswerRepository

        """create_answer_command = CreateAnswerCommand(
            'answer'
        )

        create_answer_command_handler = CreateAnswerCommandHandler(CreateAnswerUseCase(
            AnswerCreator(mock_answer_repository)
        ))

        create_answer_command_handler.execute(create_answer_command)"""


if __name__ == '__main__':
    unittest.main()
