from fastapi import APIRouter, Query
from starlette import status
from typing import List, Annotated
import uuid
from dependencies.service_dependencies import item_service
from src.schemas.items_schemas import (
    ItemForUpdate,
    ItemForPost,
    ItemForResponse,
    ItemForUpdate,
    ItemForResponseWithCategory,
)

router = APIRouter(tags=["Items"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ItemForResponseWithCategory
)
async def create_item(item: ItemForPost, service: item_service):
    return await service.create_item(item=item)


@router.get(
    "/{item_id}/",
    status_code=status.HTTP_200_OK,
    response_model=ItemForResponseWithCategory,
)
async def get_item(item_id: uuid.UUID, service: item_service):
    return await service.get_item_by_id(id=item_id)


@router.patch(
    "/{item_id}/",
    status_code=status.HTTP_200_OK,
    response_model=ItemForResponseWithCategory,
)
async def update_item(item: ItemForUpdate, service: item_service, item_id: uuid.UUID):
    return await service.update_item(id=item_id, updating_item=item)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ItemForResponse])
async def get_items_by_categories(
    service: item_service, category: Annotated[list[str] | None, Query(max_length=20)] = None
):
    return await service.get_items_by_categories(categories=category)


@router.delete("/{item_id}/", status_code=status.HTTP_200_OK)
async def delete_item(item_id: uuid.UUID, service: item_service):
    return await service.delete_item_by_id(id=item_id)
