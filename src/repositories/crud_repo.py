from ast import stmt
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from turtle import update
from pydantic import BaseModel
import uuid
from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from src.models.base import Base
from typing import Type, List
from sqlalchemy import select, delete, update
from models.category import Category
from sqlalchemy.exc import SQLAlchemyError

@dataclass
class AbstractCrudRepo(ABC):
    __model: Type[Base]
    __session: AsyncSession

    @abstractmethod
    async def create(self, model: BaseModel) -> Base:
        raise NotImplementedError
    
    @abstractmethod
    async def delete(self, id: uuid.UUID) -> Base:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, id: uuid.UUID, model: BaseModel) -> Base:
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_id(self, id: uuid.UUID) -> Base:
        raise NotImplementedError
    
@dataclass
class CrudRepo(AbstractCrudRepo):
    async def create(self, model: BaseModel) -> Base:
        new_obj = self.__model(model.model_dump())
        self.__session.add(new_obj)
        await self.__session.commit()
        return new_obj
    
    async def delete(self, id: uuid.UUID) -> Base:
        stmt = delete(self.__model).where(self.__model.id == id).returning(self.__model)
        obj = await self.__session.execute(stmt)
        await self.__session.commit()
        return obj
        
    async def update(self, id: uuid.UUID, model: BaseModel) -> Base:
        stmt = update(self.__model).where(self.__model.id).values(model.model_dump(exclude_defaults=True)).returning(self.__model)
        obj = await self.__session.execute(stmt)
        await self.__session.commit()
        return obj
 
    async def get_by_id(self, id: uuid.UUID) -> Base:
        stmt = select(self.__model).where(self.__model.id == id)
        obj = await self.__session.scalar(stmt)
        return obj
    