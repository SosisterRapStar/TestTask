from dataclasses import dataclass
from abc import ABC, abstractmethod
from re import L
from sqlalchemy import select
from sqlalchemy.orm import selectinload, contains_eager
import uuid
from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
from typing import Any, Coroutine, Type, List
from models.base import Base
from models.item import Item, Category
from src.repositories.crud_repo import AbstractCrudRepo, CrudRepo

@dataclass
class AbstractItemRepo(AbstractCrudRepo):

    @abstractmethod
    async def get_items_by_category(self, *categories) -> List[Item]:
        raise NotImplementedError
    

@dataclass
class ItemRepository(AbstractItemRepo, CrudRepo):
    __model = Item
    
    async def get_by_id(self, id: uuid.UUID) -> Item:
        stmt = select(Item).where(Item.id == id).options(selectinload(Category))
        return await self.__session.scalar(stmt)
    
    async def get_by_categories(self, *categories) -> List[Item]:
        stmt = select(Item).join(Category, Item.category_fk == Category.id).where(Category.name.in_(categories))
        # .options(contains_eager(Item.category))
        return list(await self.__session.scalars(stmt))

    
