import unittest

from unittest.mock import patch, Mock

import project
from project.application.answer.update_answer_text.update_answer_text_command import UpdateAnswerTextCommand
from project.application.answer.update_answer_text.update_answer_text_command_handler import \
    UpdateAnswerTextCommandHandler
from project.application.answer.update_answer_text.update_answer_text_use_case import UpdateAnswerTextUseCase
from project.domain.answer.answer import Answer
from project.domain.answer.exception.answer_not_found_exception import AnswerNotFoundException
from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository
from project.tests.unit.domain.answer.answer_mother import AnswerMother


class CreateAnswerCommandHandlerTest(unittest.TestCase):

    @patch('project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository')
    @patch('project.domain.answer.service.answer_finder.AnswerFinder')
    def test_update_ok(
            self,
            mock_answer_finder,
            mock_answer_repository,

    ):
        assert mock_answer_finder is project.domain.answer.service.answer_finder.AnswerFinder
        assert mock_answer_repository is project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository

        new_text: str = 'answer'
        current_answer: Answer = AnswerMother.random()
        modified_answer: Answer = AnswerMother.create(
            answer_id=current_answer.answer_id,
            text=new_text,
        )
        modified_answer.text = new_text

        update_answer_text_command = UpdateAnswerTextCommand(
            id_answer=current_answer.answer_id,
            text=new_text,
        )

        update_answer_text_command_handler = UpdateAnswerTextCommandHandler(UpdateAnswerTextUseCase(
            mock_answer_repository,
            mock_answer_finder,
        ))

        mock_answer_finder.return_value = current_answer
        mock_answer_repository.return_value = modified_answer

        result_answer = update_answer_text_command_handler.__call__(update_answer_text_command)

        self.assertEquals(result_answer.answer_id, current_answer.answer_id)
        self.assertNotEquals(result_answer.text, current_answer.text)
        self.assertEquals(result_answer.text, new_text)

    @patch('project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository')
    @patch('project.domain.answer.service.answer_finder.AnswerFinder')
    def test_create_exception_question_not_found(
            self,
            mock_answer_finder,
            mock_answer_repository,
    ):
        assert mock_answer_finder is project.domain.answer.service.answer_finder.AnswerFinder
        assert mock_answer_repository is project.infrastructure.persistence.PostgreSQL.answer.answer_repository.AnswerRepository

        new_text: str = 'answer'

        update_answer_text_command = UpdateAnswerTextCommand(
            id_answer=1,
            text=new_text,
        )

        update_answer_text_command_handler = UpdateAnswerTextCommandHandler(UpdateAnswerTextUseCase(
            mock_answer_repository,
            mock_answer_finder,
        ))

        mock_answer_finder.__call__ = Mock(return_value=None)

        self.assertRaises(AnswerNotFoundException, update_answer_text_command_handler.__call__,
                          update_answer_text_command)


if __name__ == '__main__':
    unittest.main()
