from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid
from models import item
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

@dataclass
class AbstractItemService(ABC):
    __session: AsyncSession
    
    @abstractmethod
    async def get_item(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_item_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def get_items_by_categories(self, categories: List[str]):
        raise NotImplementedError
    
    @abstractmethod
    async def update_item(self, id: uuid.UUID):
        raise NotImplementedError
    
    

        
    