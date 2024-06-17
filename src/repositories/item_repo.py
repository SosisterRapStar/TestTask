from dataclasses import dataclass
from abc import ABC, abstractmethod
from pydantic import BaseModel

from requests import session
from sqlalchemy import Result, select, update
from sqlalchemy.orm import selectinload, contains_eager
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import Any, ClassVar, Coroutine, Type, List
from models import category
from models.base import Base
from models.item import Item
from models.category import Category
from schemas.items_schemas import ItemForPost, ItemForUpdate
from src.repositories.crud_repo import AbstractCrudRepo, CrudRepo
from sqlalchemy.exc import NoResultFound


@dataclass
class CategoryNotFound(NoResultFound):
    pass
    

@dataclass
class AbstractItemRepo(AbstractCrudRepo):

    @abstractmethod
    async def get_items_by_category(self, categories: List[str]) -> List[Item]:
        raise NotImplementedError


@dataclass
class ItemRepository(AbstractItemRepo, CrudRepo):
    _model: ClassVar[Item] = Item

    async def get_by_id(self, id: uuid.UUID) -> Item:
        stmt = select(Item).where(Item.id == id).options(selectinload(Item.category))
        result: Result = await self.session.execute(stmt)
        obj = result.scalar_one()

        return obj

    async def get_items_by_category(self, *categories) -> List[Item]:
        stmt = (
            select(Item)
            .join(Category, Item.category_fk == Category.id)
            .where(Category.name.in_(categories))
        )
        # .options(contains_eager(Item.category))
        res: Result = await self.session.execute(stmt)
        objs = res.scalars().all()
        return objs
    
    async def update(self, id: uuid.UUID, model: ItemForUpdate) -> Item:
        
        new_values = await self.change_model_by_exracting_cat_id_by_name(model.model_dump(exclude_defaults=True))
        
        stmt = (
            update(self._model)
            .where(self._model.id == id)
            .values(new_values)
            .returning(self._model)
        )
        res = await self.session.execute(stmt)
        obj = res.scalar_one()
        await self.session.commit()
        await obj.awaitable_attrs.category
        return obj
    
    async def create(self, model: ItemForPost) -> Item:
        values = await self.change_model_by_exracting_cat_id_by_name(model.model_dump())
        new_obj = self._model(**values)
        self.session.add(new_obj)
        await self.session.commit()
        await new_obj.awaitable_attrs.category
        return new_obj
    
    async def change_model_by_exracting_cat_id_by_name(self, new_values: dict):
        
        if 'category_name' in new_values:
            stmt = select(Category.id).where(Category.name == new_values['category_name'])
            try:
                result = await self.session.execute(stmt)
                category_fk = result.scalar_one()
            except NoResultFound:
                raise CategoryNotFound
            
            # OMG
            del new_values['category_name']
            new_values['category_fk'] = category_fk
        return new_values
            
        