from dataclasses import dataclass
from typing import Optional

from project.domain.user.repository.user_repository import ITUserRepository
from project.domain.user.user import User


@dataclass
class UserRepository(ITUserRepository):
    def get_all(self) -> list[User]:
        return User.query.all()

    def get(self, user_id: int) -> Optional[User]:
        return User.query.get(user_id)
