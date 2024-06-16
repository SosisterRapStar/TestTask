from pydantic import BaseModel, Field
import uuid
from src.schemas.category_schemas import CategoryForResponse


class BaseItem(BaseModel):
    price: int
    amount: int
    description:str
    
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
    pass 

