import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Serving(BaseModel):
    id: uuid.UUID
    name: str
    size_g: Optional[float] = Field(default=None, gt=0.0)
    ingredient_id: uuid.UUID