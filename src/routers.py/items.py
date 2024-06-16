from fastapi import APIRouter
from starlette import status
from typing import List
import uuid
router = APIRouter(tags=["Items"])



@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_item():
    pass


@router.get("/{item_id}/", status_code=status.HTTP_200_OK)
async def get_item(id: uuid.UUID):
    pass

@router.patch("/{item_id}/", status_code=status.HTTP_200_OK)
async def update_item(item_id: uuid.UUID):
    pass


@router.get("/")
async def get_items_by_categories(q: List[str]):
    pass 

