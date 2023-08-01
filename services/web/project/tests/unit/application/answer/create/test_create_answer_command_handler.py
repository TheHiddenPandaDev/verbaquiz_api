import unittest
import project

from unittest.mock import patch

from project.application.answer.create.answer_creator import AnswerCreator
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.application.answer.create.create_answer_command import CreateAnswerCommand
from project.application.answer.create.create_answer_use_case import CreateAnswerUseCase

from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository


class CreateAnswerCommandHandlerTest(unittest.TestCase):

    @patch('project.infrastructure.persistance.PostgreeSQL.answer.answer_repository.AnswerRepository')
    @patch('project.domain.answer.service.user_finder.UserFinder')
    def test_create_ok(
            self,
            mock_answer_repository,
    ):
        assert mock_answer_repository is project.infrastructure.persistance.PostgreeSQL.answer.answer_repository.AnswerRepository

        create_answer_command = CreateAnswerCommand(
            'answer'
        )

        create_answer_command_handler = CreateAnswerCommandHandler(CreateAnswerUseCase(
            AnswerCreator(mock_answer_repository)
        ))

        create_answer_command_handler.execute(create_answer_command)


if __name__ == '__main__':
    unittest.main()
