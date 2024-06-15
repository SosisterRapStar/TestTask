
# from sqlalchemy import URL
# from asyncio import current_task
# from sqlalchemy.ext.asyncio import (
#     async_sessionmaker,
#     async_scoped_session,
#     AsyncSession,
#     AsyncAttrs,
# )
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.orm import Mapped, DeclarativeBase
# from src.config import settings
# from .annotated_types import UUIDpk


# class Base(AsyncAttrs, DeclarativeBase):
#     __abstract__ = True
#     id: Mapped[UUIDpk]

#     def __repr__(self):
#         return f"{self.__class__.__name__}: {self.id}"

#     def __str__(self):
#         return self.__repr__()
    
