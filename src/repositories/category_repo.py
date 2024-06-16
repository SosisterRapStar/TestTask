from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pydantic import BaseModel
import uuid
from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
from typing import Type


@dataclass
class AbstractCategoryRepo(ABC):
    __model: Type[DeclarativeBase] = field(default=None)
    __session: AsyncSession

    @abstractmethod
    def create_category(self, model: BaseModel):
        raise NotImplementedError
    
    @abstractmethod
    def delete_category(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    def update_category(self, model: BaseModel):
        raise NotImplementedError