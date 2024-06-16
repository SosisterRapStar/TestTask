from .session_dep import session_dep
from src.repositories.item_repo import AbstractItemRepo, ItemRepository
from src.repositories.category_repo import AbstractCategoryRepo, CategoryRepo

def get_item_repo(session: session_dep) -> AbstractItemRepo:
    return ItemRepository(session=session)

def get_category_repo(session: session_dep) -> AbstractCategoryRepo:
    return CategoryRepo(session=session)