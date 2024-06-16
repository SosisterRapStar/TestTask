from .base import Base
from sqlalchemy import ForeignKey, Table, Column, Integer, UniqueConstraint, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from item import Item

class Category(Base):
    __tablename__ = "categories"

    name: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    items: Mapped["Item"] = relationship(back_populates="category", uselist=True,
                                         cascade="all, delete",
                                         passive_deletes=True,)
    description: Mapped[str] | None = mapped_column(String(200), nullable=True)
    
