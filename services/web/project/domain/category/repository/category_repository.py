from abc import ABC
from typing import Optional

from project.domain.category.category import Category


class ITCategoryRepository(ABC):
    def get_all(self) -> None:
        ...

    def get(self, category_id: int) -> Optional[Category]:
        ...
