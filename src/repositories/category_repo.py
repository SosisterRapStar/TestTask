from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Type, List, ClassVar
from sqlalchemy import Result, select
from models.category import Category
from src.repositories.crud_repo import AbstractCrudRepo, CrudRepo


@dataclass
class AbstractCategoryRepo(AbstractCrudRepo):

    @abstractmethod
    async def get_categories(self) -> Category:
        raise NotImplementedError


@dataclass
class CategoryRepo(AbstractCategoryRepo, CrudRepo):
    _model: ClassVar[Category] = Category

    async def get_categories(self) -> List[Category]:
        stmt = select(Category)
        res: Result = await self.session.execute(stmt)
        objs = await res.all()
        return list(objs)
