from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base import DatabaseHandler


async def get_session() -> AsyncSession:
    return DatabaseHandler.get_scoped_session()

session_dep = Annotated[AsyncSession, Depends(get_session)]