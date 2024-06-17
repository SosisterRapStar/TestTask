from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.base import DatabaseHandler


async def get_session() -> AsyncSession:
    session = DatabaseHandler.get_scoped_session()
    async with session() as session:
        yield session


session_dep = Annotated[AsyncSession, Depends(get_session)]
