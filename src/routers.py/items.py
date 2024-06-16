from fastapi import APIRouter
from starlette import status

router = APIRouter(tags=["Items"])



@router.post("/create", status_code=status.HTTP_201_CREATED)

