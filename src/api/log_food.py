from fastapi import APIRouter, Depends
from supabase import Client

from core import auth
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
