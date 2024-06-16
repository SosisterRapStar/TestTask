from fastapi import APIRouter, Query
from starlette import status
from typing import List, Annotated
import uuid
router = APIRouter(tags=["Items"])



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item():
    pass


@router.get("/{item_id}/", status_code=status.HTTP_200_OK)
async def get_item(item_id: uuid.UUID):
    pass

@router.patch("/{item_id}/", status_code=status.HTTP_200_OK)
async def update_item(item_id: uuid.UUID):
    pass


@router.get("/")
async def get_items_by_categories(q: Annotated[list[str] | None, Query(max_length=20)] = None):
    pass 


@router.delete("/{item_id}/", status_code=status.HTTP_200_OK)
async def delete_item(item_id: uuid.UUID):
    pass
