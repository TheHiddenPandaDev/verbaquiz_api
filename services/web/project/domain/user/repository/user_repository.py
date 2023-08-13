from abc import ABC
from typing import Optional

from project.domain.user.user import User


class ITUserRepository(ABC):
    def get_all(self) -> None:
        ...

    def get(self, user_id: int) -> Optional[User]:
        ...
