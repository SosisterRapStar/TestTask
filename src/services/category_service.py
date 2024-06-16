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
    __repository: AbstractCategoryRepo
    
    @abstractmethod
    async def create_category(self, category: CategoryForPost):
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
    
    
@dataclass
class CategoryService(AbstractCategoryService):
    async def create_category(self, category: CategoryForPost):
        return await self.__repository.create(model=category)
    
    async def get_category_by_id(self, id: uuid.UUID):
        return await self.__repository.get_by_id(id=id)
    
    async def get_categories(self):
        return await self.__repository.get_categories()
    
    async def delete_category_by_id(self, id: uuid.UUID):
        return await self.__repository.delete(id=id)
    
    async def update_category(self, id: uuid.UUID, updating_category: CategoryForUpdate):
        return await self.__repository.update(id=id, model=updating_category)
    
    

        
    