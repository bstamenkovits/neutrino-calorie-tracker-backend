import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    id: uuid.UUID

    category_id: Optional[uuid.UUID] = None
    added_by_user_id: Optional[uuid.UUID] = None
    date_added: Optional[datetime.datetime] = Field(default=None, ge=datetime.datetime.now)

    name: str
    calories_kcal: Optional[float] = Field(default=None, ge=0.0)
    fat_g: Optional[float] = Field(default=None, ge=0.0)
    carbs_g: Optional[float] = Field(default=None, ge=0.0)
    protein_g: Optional[float] = Field(default=None, ge=0.0)