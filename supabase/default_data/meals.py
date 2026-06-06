from pydantic import BaseModel

from neutrino.core.database.supabase_client import supabase_client
from neutrino.core.models.meal import Meal

meals = [
    Meal(name="Breakfast"),
    Meal(name="Lunch"),
    Meal(name="Dinner"),
    Meal(name="Snacks"),
]

data = [meal.model_dump(mode="json") for meal in meals]

# supabase_client.schema("app").table("meals").insert(data).execute()

meal_data = supabase_client.schema("app").table("meals").select("*").execute()
print(meal_data)