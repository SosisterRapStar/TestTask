from fastapi import APIRouter, Query
from starlette import status
from typing import List, Annotated
import uuid
from src.services.category_service import AbstractCategoryService
from src.schemas.category_schemas import CategoryForPost, CategoryForUpdate, CategoryForResponse


from models import category
router = APIRouter(tags=["Categories"])



@router.get("/", status_code=status.HTTP_200_OK, response_model=List[CategoryForResponse])
async def get_categories(service: AbstractCategoryService):
    return await service.get_categories()

@router.get("/{category_id}/", response_model=CategoryForResponse)
async def get_category(category_id: uuid.UUID, service: AbstractCategoryService):
    return await service.get_category_by_id(id=category_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryForResponse)
async def create_category(category: CategoryForPost, service: AbstractCategoryService):
    return await service.create_category(category=category)

@router.delete("/{category_id}/", status_code=status.HTTP_200_OK, response_model=CategoryForResponse)
async def delete_category(service: AbstractCategoryService, category_id: uuid.UUID):
    return await service.delete_category_by_id(id=category_id)
    


