from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pydantic import BaseModel
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from models import category
from src.models.base import Base
from typing import Type, List, ClassVar
from sqlalchemy import Result, select, delete, update
from models.category import Category
from sqlalchemy.exc import SQLAlchemyError


@dataclass
class AbstractCrudRepo(ABC):
    session: AsyncSession

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
    _model: ClassVar[Type[Base]] = None
    
    async def create(self, model: BaseModel) -> Base:
        new_obj = self._model(**model.model_dump())
        self.session.add(new_obj)
        await self.session.commit()
        return new_obj

    async def delete(self, id: uuid.UUID) -> Base:
        stmt = delete(self._model).where(self._model.id == id).returning(self._model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def update(self, id: uuid.UUID, model: BaseModel) -> Base:
        
        stmt = (
            update(self._model)
            .where(self._model.id == id)
            .values(model.model_dump(exclude_defaults=True))
            .returning(self._model)
        )
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def get_by_id(self, id: uuid.UUID) -> Base:
        stmt = select(self._model).where(self._model.id == id)
        res: Result = await self.session.execute(stmt)
        return res.scalar_one()
