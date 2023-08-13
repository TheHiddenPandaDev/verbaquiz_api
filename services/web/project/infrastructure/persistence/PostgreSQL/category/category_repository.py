from dataclasses import dataclass
from typing import Optional

from project.domain.category.repository.category_repository import ITCategoryRepository
from project.domain.category.category import Category


@dataclass
class CategoryRepository(ITCategoryRepository):
    def get_all(self) -> list[Category]:
        return Category.query.all()

    def get(self, category_id: int) -> Optional[Category]:
        return Category.query.get(category_id)
