from .base import Base
from sqlalchemy import ForeignKey, Table, Column, Integer, UniqueConstraint, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .annotated_types import UUIDpk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from category import Category


class Item(Base):
    __tablename__ = "items"

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    category: Mapped["Category"] = relationship(back_populates="items", uselist=False)
    category_fk: Mapped[UUIDpk] = mapped_column(
        ForeignKey("categories.id", ondelete="Cascade")
    )
    description: Mapped[str | None] = mapped_column(String(200))
