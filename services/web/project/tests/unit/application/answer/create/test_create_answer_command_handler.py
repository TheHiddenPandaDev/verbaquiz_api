import unittest

from unittest.mock import patch, Mock

import project
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.application.answer.create.create_answer_command import CreateAnswerCommand
from project.application.answer.create.create_answer_use_case import CreateAnswerUseCase
from project.domain.question.exception.question_not_found_exception import QuestionNotFoundException
from project.domain.question.question import Question

from project.domain.question.service.question_finder import QuestionFinder
from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository
from project.tests.unit.domain.question.question_mother import QuestionMother


class CreateAnswerCommandHandlerTest(unittest.TestCase):

    @patch('project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository')
    @patch('project.domain.question.service.question_finder.QuestionFinder')
    def test_create_ok(
            self,
            mock_question_finder,
            mock_answer_repository,

    ):
        assert mock_question_finder is project.domain.question.service.question_finder.QuestionFinder
        assert mock_answer_repository is project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository

        question: Question = QuestionMother.random()

        create_answer_command = CreateAnswerCommand(
            question_id=1,
            text='answer',
        )

        create_answer_command_handler = CreateAnswerCommandHandler(CreateAnswerUseCase(
            mock_answer_repository,
            mock_question_finder,
        ))

        mock_question_finder.__call__ = Mock(return_value=question)

        create_answer_command_handler.__call__(create_answer_command)

    @patch('project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository')
    @patch('project.domain.question.service.question_finder.QuestionFinder')
    def test_create_exception_question_not_found(
            self,
            mock_question_finder,
            mock_answer_repository,
    ):
        assert mock_question_finder is project.domain.question.service.question_finder.QuestionFinder
        assert mock_answer_repository is project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository

        create_answer_command = CreateAnswerCommand(
            question_id=1,
            text='answer',
        )

        create_answer_command_handler = CreateAnswerCommandHandler(CreateAnswerUseCase(
            mock_answer_repository,
            mock_question_finder,
        ))

        mock_question_finder.__call__ = Mock(return_value=None)

        self.assertRaises(QuestionNotFoundException, create_answer_command_handler.__call__, create_answer_command)


if __name__ == '__main__':
    unittest.main()
