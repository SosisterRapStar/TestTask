from pydantic import BaseModel, Field, ConfigDict
import uuid
from src.schemas.category_schemas import CategoryForResponse


class BaseItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    price: int
    amount: int
    description: str


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
    price: int = Field(default=None)
    amount: int = Field(default=None)
    category_name: str = Field(max_length=20, default=None)
    description: str = Field(default=None, max_length=200, default=None)
