from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pydantic import BaseModel
import uuid

@dataclass
class Abstract(ABC):
    model: Type[Base] = field(default=None)

    @abstractmethod
    def create_category(self, model: BaseModel):
        raise NotImplementedError
    
    @abstractmethod
    def delete_category(self, id: uuid.UUID):
        raise NotImplementedError
    
    @abstractmethod
    def update_category(self, model: BaseModel):
        raise NotImplementedError