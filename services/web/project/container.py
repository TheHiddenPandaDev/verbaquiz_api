from dependency_injector import containers, providers

from project.infrastructure.persistance.PostgreeSQL.answer.answer_repository import AnswerRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Domain Layer
    answer_repository = providers.Singleton(AnswerRepository)