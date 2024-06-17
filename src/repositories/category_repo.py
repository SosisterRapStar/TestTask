from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Type, List
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
    __model = Category
    
    async def  get_categories(self) -> List[Category]:
        stmt = select(Category)
        res: Result = await self.__session.execute(stmt)
        objs = await res.all()
        return list(objs)
 
