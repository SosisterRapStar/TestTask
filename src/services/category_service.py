from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid
from models.category import Category
from sqlalchemy.ext.asyncio import AsyncSession

@dataclass
class AbstractCategoryService(ABC):
    __session: AsyncSession
    
    @abstractmethod
    async def get_category_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_category_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def update_category(self, id: uuid.UUID):
        raise NotImplementedError
    
    

        
    