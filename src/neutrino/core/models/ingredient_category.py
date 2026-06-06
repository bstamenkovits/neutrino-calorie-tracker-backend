import uuid
from pydantic import BaseModel


class IngredientsCategory(BaseModel):
    id: uuid.UUID
    name: str


