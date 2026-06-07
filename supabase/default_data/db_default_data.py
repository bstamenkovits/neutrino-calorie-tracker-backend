import pandas as pd
from neutrino.core.models.ingredient_category import IngredientsCategory
from neutrino.core.models.ingredient import Ingredient
from neutrino.core.database.supabase_client import supabase_client


# 001_ingredient_categories
def create_ingredient_categories_data():
    ingredient_data = pd.read_csv("ingredients.csv")

    categories = ingredient_data["Type"].unique().tolist()

    ingredient_category_data = [
        IngredientsCategory(name=cat).model_dump(mode="json")
        for cat in categories
    ]

    supabase_client.schema("app").table("ingredient_categories").insert(ingredient_category_data).execute()

    data = supabase_client.schema("app").table("ingredient_categories").select("*").execute()
    print(f"Ingredient Categories: {data}")


# 002_ingredients
def create_ingredient_data():
    ingredient_data_raw = pd.read_csv("ingredients.csv")
    ingredient_category_data = supabase_client.schema("app").table("ingredient_categories").select("*").execute()
    ingredient_category_map = {row['name']: row['id'] for row in ingredient_category_data.data}

    ingredient_data = []
    for idx, row in ingredient_data_raw.iterrows():
        ingredient = Ingredient(
            category_id = ingredient_category_map[row['Type']],
            name=row['Name'],
            calories_kcal=row['Calories (kcal)'],
            fat_g=row['Fat (g)'],
            carbs_g=row['Carbs (g)'],
            protein_g=row['Protein (g)'],
        ).model_dump(mode="json")
        ingredient_data.append(ingredient)

    supabase_client.schema("app").table("ingredients").insert(ingredient_data).execute()

    data = supabase_client.schema("app").table("ingredients").select("*").execute()
    print(f"Ingredient Categories: {data}")


if __name__ == "__main__":
    create_ingredient_categories_data()
    create_ingredient_data()
