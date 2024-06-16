from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import N
import uuid
from models import item
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from repositories.item_repo import AbstractItemRepo
from schemas.items_schemas import ItemForPost, ItemForUpdate

@dataclass
class AbstractItemService(ABC):
    __session: AsyncSession
    __repository: AbstractItemRepo
    
    @abstractmethod
    async def get_item_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    
    @abstractmethod
    async def delete_item_by_id(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    async def get_items_by_categories(self, categories: List[str]):
        raise NotImplementedError
    
    @abstractmethod
    async def update_item(self, id: uuid.UUID, updating_item: ItemForUpdate):
        raise NotImplementedError
    
    @abstractmethod
    async def create_item(item: ItemForPost):
        raise NotImplementedError
    
    

        
    