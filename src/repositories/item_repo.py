from dataclasses import dataclass
from abc import ABC, abstractmethod
from pydantic import BaseModel
import uuid
from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase
from typing import Type, List

@dataclass
class AbstractItemRepo(ABC):
    __model: Type[DeclarativeBase]
    __session: AsyncSession

    @abstractmethod
    def create_item(self, model: BaseModel) -> Type[DeclarativeBase]:
        raise NotImplementedError
    
    @abstractmethod
    def delete_item(self, id: uuid.UUID) -> uuid.UUID:
        raise NotImplementedError
    
    @abstractmethod
    def update_item(self, model: BaseModel) -> Type[DeclarativeBase]:
        raise NotImplementedError
    
    @abstractmethod
    def get_items_by_category(self, *categories) -> List | None:
        raise NotImplementedError
    

    
