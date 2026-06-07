import pandas as pd
from neutrino.core.models.ingredient_category import IngredientsCategory
from neutrino.core.database.supabase_client import supabase_client

ingredient_data = pd.read_csv("ingredients.csv")

categories = ingredient_data["Type"].unique().tolist()

ingredient_category_data = [
    IngredientsCategory(name=cat).model_dump(mode="json") for cat in categories
]

supabase_client.schema("app").table("ingredients_categories").insert(ingredient_category_data).execute()

data = supabase_client.schema("app").table("ingredients_categories").select("*").execute()
print(data)