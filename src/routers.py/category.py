from fastapi import APIRouter, Query
from starlette import status
from typing import List, Annotated
import uuid

from models import category
router = APIRouter(tags=["Categories"])



@router.get("/", status_code=status.HTTP_200_OK)
async def get_categories():
    pass


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category():
    pass

@router.delete("/{category_id}/", status_code=status.HTTP_200_OK)
async def delete_category():
    pass


