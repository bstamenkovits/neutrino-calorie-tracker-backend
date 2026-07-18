import uuid
from typing import Optional
from pydantic import BaseModel, Field
import datetime


class Serving(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    size_g: float
    ingredient_id: uuid.UUID | None
    date_created: datetime.datetime = Field(default_factory=datetime.datetime.now)
    date_modified: datetime.datetime = Field(default_factory=datetime.datetime.now)