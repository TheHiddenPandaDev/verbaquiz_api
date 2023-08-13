from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistence.PostgreSQL.user.user_repository import UserRepository
from ..user import User


@dataclass
class UserFinder:
    user_repository: UserRepository

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    def __call__(
            self,
            user_id: int
    ) -> Optional[User]:
        return self.user_repository.get(
            user_id
        )
