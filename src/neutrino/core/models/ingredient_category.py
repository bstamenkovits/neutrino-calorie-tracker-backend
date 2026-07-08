import datetime
import uuid
from pydantic import BaseModel, Field


class IngredientsCategory(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    date_created: datetime.datetime = Field(default_factory=datetime.datetime.now)
    date_modified: datetime.datetime = Field(default_factory=datetime.datetime.now)
