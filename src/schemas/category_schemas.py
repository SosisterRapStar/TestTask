import uuid
from pydantic import BaseModel, Field




    
class BaseCategory(BaseModel):
    name: str
    description: str
    
class CategoryWithId(BaseCategory):
    id: uuid.UUID
    
class CategoryForResponse(CategoryWithId):
    pass

class CategotyForPost(BaseCategory):
    description: str = Field(default=None, max_length=200)
    name: str = Field(max_length=20)

class CategoryForUpdate(CategotyForPost):
    pass
    

