import datetime
import uuid
from pydantic import BaseModel, Field


class IngredientsCategory(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    date_added: datetime.datetime = Field(default_factory=datetime.datetime.now)
    date_last_updated: datetime.datetime = Field(default_factory=datetime.datetime.now)
