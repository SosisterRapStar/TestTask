from dataclasses import dataclass
from abc import ABC, abstractmethod
from re import I
import uuid
from models.category import Category
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.category_repo import AbstractCategoryRepo
from src.schemas.category_schemas import CategoryForPost, CategoryForUpdate
@dataclass
class AbstractCategoryService(ABC):
    __session: AsyncSession
    __repository: AbstractCategoryRepo
    
    @abstractmethod
    async def create_category(category: CategoryForPost):
        raise NotImplementedError
    
    @abstractmethod
    async def get_category_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def get_categories(self):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_category_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def update_category(self, id: uuid.UUID, updating_category: CategoryForUpdate):
        raise NotImplementedError
    
    

        
    