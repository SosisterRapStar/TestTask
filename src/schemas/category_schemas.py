import uuid
from pydantic import BaseModel, Field, ConfigDict


class BaseCategory(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)
    description: str | None = Field(default=None, max_length=200)
    name: str = Field(max_length=20)


class CategoryWithId(BaseCategory):
    id: uuid.UUID


class CategoryForResponse(CategoryWithId):
    pass


class CategoryForPost(BaseCategory):
    pass


class CategoryForUpdate(CategoryForPost):
    description: str = Field(default=None, max_length=200)
    name: str = Field(default=None, max_length=20)
