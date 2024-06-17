from typing import Annotated

from fastapi import Depends
from .session_dep import session_dep
from src.repositories.item_repo import ItemRepository
from src.repositories.category_repo import CategoryRepo
from src.services.category_service import CategoryService, AbstractCategoryService
from src.services.item_service import ItemService, AbstractItemService


def get_category_service(session: session_dep) -> AbstractCategoryService:
    return CategoryService(repository=CategoryRepo(session=session))


def get_item_service(session: session_dep) -> AbstractItemService:
    return ItemService(repository=ItemRepository(session=session))


item_service = Annotated[AbstractItemService, Depends(get_item_service)]
category_service = Annotated[AbstractCategoryService, Depends(get_category_service)]
