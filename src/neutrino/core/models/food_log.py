import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class FoodLog(BaseModel):
    id: uuid.UUID
    user_id: Optional[uuid.UUID] = None
    date_added: datetime
    meal_id: Optional[uuid.UUID] = None
    ingredient_id: Optional[uuid.UUID] = None
    serving_id: Optional[uuid.UUID] = None
    quantity: float


