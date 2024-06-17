from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid
from models.item import Item
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from repositories.item_repo import AbstractItemRepo
from schemas.items_schemas import ItemForPost, ItemForUpdate
from .HTTPexc import ItemNotFoundHTTPException, SomeErrorHTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError

@dataclass
class AbstractItemService(ABC):
    repository: AbstractItemRepo
    
    @abstractmethod
    async def get_item_by_id(self, id: uuid.UUID) -> Item:
        raise NotImplementedError
    
    
    @abstractmethod
    async def delete_item_by_id(self, id: uuid.UUID) -> Item:
        raise NotImplementedError
    
    @abstractmethod
    async def get_items_by_categories(self, categories: List[str]) -> Item:
        raise NotImplementedError
    
    @abstractmethod
    async def update_item(self, id: uuid.UUID, updating_item: ItemForUpdate) -> Item:
        raise NotImplementedError
    
    @abstractmethod
    async def create_item(self, item: ItemForPost) -> Item:
        raise NotImplementedError
    
    
    
    
    


@dataclass
class ItemService(AbstractItemService):
    async def get_item_by_id(self, id: uuid.UUID) -> Item:
        try:
            return await self.__repository.get_by_id(id=id)
        except NoResultFound:
            raise ItemNotFoundHTTPException()
    
    async def delete_item_by_id(self, id: uuid.UUID) -> Item:
        try:
            return await self.__repository.delete(id=id)
        except NoResultFound:
            raise ItemNotFoundHTTPException()
    
    async def get_items_by_categories(self, categories: List[str]) -> Item:
        try:
            return await self.__repository.get_items_by_category(categories)
        except NoResultFound:
            raise ItemNotFoundHTTPException()
    
    async def update_item(self, id: uuid.UUID, updating_item: ItemForUpdate) -> Item:
        try:
            return await self.__repository.update(model=updating_item, id=id)
        except NoResultFound:
            raise ItemNotFoundHTTPException()
        except IntegrityError:
            raise SomeErrorHTTPException()
    
    
    async def create_item(self, item: ItemForPost) -> Item:
        try:
            return await self.__repository.create(model=item)
        except IntegrityError:
            raise SomeErrorHTTPException()
            