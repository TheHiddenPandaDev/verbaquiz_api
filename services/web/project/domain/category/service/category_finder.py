from dataclasses import dataclass
from typing import Optional

from project.infrastructure.persistence.PostgreSQL.category.category_repository import CategoryRepository
from ..category import Category


@dataclass
class CategoryFinder:
    category_repository: CategoryRepository

    def __init__(
        self,
        category_repository: CategoryRepository,
    ):
        self.category_repository = category_repository

    def __call__(
            self,
            category_id: int
    ) -> Optional[Category]:
        return self.category_repository.get(
            category_id
        )
