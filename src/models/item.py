from base import Base
from sqlalchemy import ForeignKey, Table, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column
from annotated_types import UUIDpk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from category import Category

class Item(Base):
    __tablename__ = "items"

    price: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
    category: Mapped["Category"] = relationship(back_populates="items", uselist=False)
    category_fk: Mapped[UUIDpk] = mapped_column(ForeignKey("categories.id", ondelete="Cascade"))
