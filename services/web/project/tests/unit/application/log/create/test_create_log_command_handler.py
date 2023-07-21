import unittest
import project

from unittest.mock import patch, Mock
from faker import Faker

from project.application.log.create.create_log_command_handler import CreateLogCommandHandler
from project.application.log.create.create_log_command import CreateLogCommand
from project.application.log.create.create_log_use_case import CreateLogUseCase

from project.domain.user.exception.user_not_found_exception import UserNotNotFoundException
from project.domain.user.service.user_finder import UserFinder
from project.domain.user.user import User
from project.infrastructure.persistance.PostgreeSQL.log.log_repository import LogRepository
from project.tests.unit.domain.user.user_mother import UserMother

class CreateLogCommandHandlerTest(unittest.TestCase):

    @patch('project.infrastructure.persistance.PostgreeSQL.answer.log_repository.LogRepository')
    @patch('project.domain.answer.service.user_finder.UserFinder')
    def test_create_ok(
        self,
        MockUserFinder,
        MockLogRepository,
    ):

        assert MockUserFinder is project.domain.user.service.user_finder.UserFinder
        assert MockLogRepository is project.infrastructure.persistance.PostgreeSQL.log.log_repository.LogRepository

        user_doing_action: User = UserMother.random()
        user_referred: User = UserMother.random()

        create_log_command = CreateLogCommand(
            'action',
            user_doing_action.user_id,
            user_referred.user_id,
            'description',
        )

        create_log_command_handler = CreateLogCommandHandler(CreateLogUseCase(
            MockLogRepository,
            MockUserFinder,
        ))

        MockUserFinder.__call__ = Mock(side_effect=[user_doing_action, user_referred])

        create_log_command_handler.__call__(create_log_command)

    @patch('project.infrastructure.persistance.PostgreeSQL.answer.log_repository.LogRepository')
    @patch('project.domain.answer.service.user_finder.UserFinder')
    def test_create_exception_user_not_found(
        self,
        MockUserFinder,
        MockLogRepository,
    ):
        assert MockUserFinder is project.domain.user.service.user_finder.UserFinder
        assert MockLogRepository is project.infrastructure.persistance.PostgreeSQL.log.log_repository.LogRepository

        user_doing_action: User = UserMother.random()
        fake: Faker = Faker()

        create_log_command = CreateLogCommand(
            'action',
            user_doing_action.user_id,
            fake.random_int(),
            'description',
        )

        create_log_command_handler = CreateLogCommandHandler(CreateLogUseCase(
            MockLogRepository,
            MockUserFinder,
        ))

        MockUserFinder.__call__ = Mock(side_effect=[user_doing_action, None])

        self.assertRaises(UserNotNotFoundException, create_log_command_handler.__call__, create_log_command)

if __name__ == '__main__':
    unittest.main()