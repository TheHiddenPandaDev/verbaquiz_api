from typing import Optional
from faker import Faker

from project.domain.user.user import User

class UserMother:

    @staticmethod
    def create(
        user_id: int,
        email: str
    ) -> User:
        return User(
            user_id=user_id,
            email=email,
        )

    @staticmethod
    def random(
        user_id: Optional[int] = None,
        email: Optional[str] = None,
    ) -> User:

        fake: Faker = Faker()

        return UserMother.create(
            user_id or fake.random_int(),
            email or fake.email(),
        )

