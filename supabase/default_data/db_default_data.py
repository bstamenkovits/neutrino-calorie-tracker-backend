import pandas as pd

from neutrino.core.database.supabase_client import supabase_client

from neutrino.core.models.ingredient_category import IngredientsCategory
from neutrino.core.models.ingredient import Ingredient
from neutrino.core.models.serving import Serving
from neutrino.core.models.meal import Meal
from neutrino.core.models.food_log import FoodLog




# 001_ingredient_categories
def create_ingredient_categories_data():
    ingredient_data = pd.read_csv("ingredients.csv")

    categories = ingredient_data["Type"].unique().tolist()

    ingredient_category_data = [
        IngredientsCategory(name=cat).model_dump(mode="json")
        for cat in categories
    ]

    supabase_client.schema("app").table("ingredient_categories").insert(ingredient_category_data).execute()


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


# 003 servings
def create_servings_data():
    ingredient_data_raw = pd.read_csv("ingredients.csv")
    ingredient_category_data = supabase_client.schema("app").table("ingredients").select("*").execute()
    ingredient_category_map = {row['name']: row['id'] for row in ingredient_category_data.data}

    servings = [
        Serving(
            name=row['Serving Name'],
            size_g=row['Single Serving (g)'],
            ingredient_id=ingredient_category_map[row['Name']],
        )
        for _, row in ingredient_data_raw.iterrows()
    ]
    servings.append(Serving(name='gram(s)', size_g=1, ingredient_id=None))

    servings_data = [serving.model_dump(mode="json") for serving in servings]
    supabase_client.schema("app").table("servings").insert(servings_data).execute()


# 004 meals
def create_meals_data():
    meals = [
        Meal(name="Breakfast"),
        Meal(name="Lunch"),
        Meal(name="Dinner"),
        Meal(name="Snacks"),
    ]

    data = [meal.model_dump(mode="json") for meal in meals]
    supabase_client.schema("app").table("meals").insert(data).execute()


#005 food logs
def create_food_logs_data():
    ingredients = supabase_client.schema("app").table("ingredients").select("*").limit(20).execute()
    meals = supabase_client.schema("app").table("meals").select("*").execute()


    food_log_data = []
    for i in range(20):
        j = i % len(meals.data)
        meal_id = meals.data[j]['id']
        ingredient_id = ingredients.data[i]['id']
        servings = supabase_client.schema("app").table("servings").select("*").filter("ingredient_id", "eq", ingredient_id).execute()
        serving_id = servings.data[0]['id']

        food_log_data.append(
            FoodLog(
                meal_id=meal_id,
                ingredient_id=ingredient_id,
                serving_id=serving_id,
                quantity=i
            ).model_dump(mode="json")
        )

    supabase_client.schema("app").table("food_logs").insert(food_log_data).execute()



if __name__ == "__main__":
    # create_ingredient_categories_data()
    # create_ingredient_data()
    # create_servings_data()
    # create_meals_data()
    create_food_logs_data()
