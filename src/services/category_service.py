from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid
from src.repositories.category_repo import AbstractCategoryRepo
from src.schemas.category_schemas import CategoryForPost, CategoryForUpdate
from .HTTPexc import SomeErrorHTTPException, CategoryNotFoundHTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError


@dataclass
class AbstractCategoryService(ABC):
    repository: AbstractCategoryRepo

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
    async def update_category(
        self, id: uuid.UUID, updating_category: CategoryForUpdate
    ):
        raise NotImplementedError


@dataclass
class CategoryService(AbstractCategoryService):
    async def create_category(self, category: CategoryForPost):
        try:
            return await self.repository.create(model=category)
        except IntegrityError:
            raise SomeErrorHTTPException()

    async def get_category_by_id(self, id: uuid.UUID):
        try:
            return await self.repository.get_by_id(id=id)
        except NoResultFound:
            raise CategoryNotFoundHTTPException()

    async def get_categories(self):
        try:
            return await self.repository.get_categories()
        except NoResultFound:
            raise CategoryNotFoundHTTPException()

    async def delete_category_by_id(self, id: uuid.UUID):
        try:
            return await self.repository.delete(id=id)
        except NoResultFound:
            raise CategoryNotFoundHTTPException()

    async def update_category(
        self, id: uuid.UUID, updating_category: CategoryForUpdate
    ):
        try:
            return await self.repository.update(id=id, model=updating_category)
        except NoResultFound:
            raise CategoryNotFoundHTTPException()
        except IntegrityError:
            raise SomeErrorHTTPException()
