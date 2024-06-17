from pydantic import BaseModel, Field, ConfigDict
import uuid
from src.schemas.category_schemas import CategoryForResponse


class BaseItem(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)
    price: int
    amount: int
    name: str = Field(max_length=100)
    description: str | None = Field(default=None)


class ItemWithId(BaseItem):
    id: uuid.UUID


class ItemForResponse(ItemWithId):
    pass


class ItemForResponseWithCategory(ItemForResponse):
    category: CategoryForResponse


class ItemForPost(BaseItem):
    price: int
    amount: int
    category_name: str = Field(max_length=20)
    description: str = Field(default=None, max_length=200)


class ItemForUpdate(ItemForPost):
    price: int | None = Field(default=None)
    amount: int | None = Field(default=None)
    name: str | None = Field(default=None)
    category_name: str  | None= Field(max_length=20, default=None)
    description: str | None = Field(default=None, max_length=200)
