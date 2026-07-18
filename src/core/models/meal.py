import uuid
from pydantic import BaseModel, Field


class Meal(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
