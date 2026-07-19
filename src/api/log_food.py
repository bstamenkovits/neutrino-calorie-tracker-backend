from fastapi import APIRouter, Depends
from supabase import Client

from core import auth
from core.models.food_log import FoodLog
from core.models.ingredient import Ingredient

router = APIRouter(
    prefix="/food",
    tags=["food"],
    # always verify the JWT token
    dependencies=[Depends(auth.verify_token)],
)


@router.get("/list-ingredients")
async def list_ingredients(db:Client = Depends(auth.get_supabase_client)):
    response = db.schema("app").table("ingredients").select("*").execute()
    return [Ingredient(**row) for row in response.data]


@router.get("/list-meals")
async def list_meals(db:Client = Depends(auth.get_supabase_client)):
    response = db.schema("app").table("meals").select("*").execute()
    return [Ingredient(**row) for row in response.data]


@router.get("/list-servings")
async def list_ingredients(ingredient_id:str|None = None, db:Client = Depends(auth.get_supabase_client)):
    query = db.schema("app").table("servings").select("*")
    if ingredient_id:
        query = query.filter("ingredient_id", "eq", ingredient_id)

    response = query.execute()
    return [Ingredient(**row) for row in response.data]


@router.post("/add-food-log")
async def add_food_log(log:FoodLog, db:Client = Depends(auth.get_supabase_client), user= Depends(auth.get_user_data)):
    log.user_id = user.id
    response = db.schema("app").table("food_logs").insert(log.model_dump(mode='json')).execute()
    return response.data


@router.get("/get-logs")
async def get_food_logs(db:Client = Depends(auth.get_supabase_client), user= Depends(auth.get_user_data)):
    query = db.schema("app").table("food_logs").select("*")
    query.filter("user_id", "eq", user.id)
    query.filter("consumed_on", "eq", "2026-07-19")

    response = query.execute()
    return [FoodLog(**row) for row in response.data]