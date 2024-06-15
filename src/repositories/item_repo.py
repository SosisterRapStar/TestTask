from dataclasses import dataclass
from abc import ABC, abstractmethod
from pydantic import BaseModel
import uuid
from sqlalchemy.ext.asyncio import (
    AsyncSession
)

@dataclass
class AbstractItemRepo(ABC):
    __model: Type[Base]
    __session: AsyncSession

    @abstractmethod
    def create_item(self, model: BaseModel):
        raise NotImplementedError
    
    @abstractmethod
    def delete_item(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    def update_item(self, model: BaseModel):
        raise NotImplementedError
    

    
