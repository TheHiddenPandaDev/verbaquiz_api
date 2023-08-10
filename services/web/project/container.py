from dependency_injector import containers, providers

from project.application.answer.create.answer_creator import AnswerCreator
from project.application.answer.create.create_answer_command_handler import CreateAnswerCommandHandler
from project.application.answer.create.create_answer_use_case import CreateAnswerUseCase
from project.domain.question.service.question_finder import QuestionFinder
from project.infrastructure.persistence.PostgreSQL.answer.answer_repository import AnswerRepository
from project.infrastructure.persistence.PostgreSQL.question.question_repository import QuestionRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    """
    ##########################################
    ### - Domain Layer                     ###
    ##########################################
    """

    answer_repository = providers.Singleton(AnswerRepository)
    question_repository = providers.Singleton(QuestionRepository)

    question_finder = providers.Factory(QuestionFinder, question_repository=question_repository)

    """
    ##########################################
    ### - Application Layer                ###
    ##########################################
    """

    # Answer - Create

    answer_creator = providers.Factory(AnswerCreator, answer_repository=answer_repository)
    create_answer_use_case = providers.Factory(
        CreateAnswerUseCase,
        answer_creator=answer_creator,
        question_finder=question_finder
    )
    create_answer_command_handler = providers.Factory(
        CreateAnswerCommandHandler,
        create_answer_use_case=create_answer_use_case
    )
