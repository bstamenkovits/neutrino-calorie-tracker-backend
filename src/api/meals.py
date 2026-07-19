from fastapi import APIRouter, Depends
from supabase import Client

from core import auth

router = APIRouter(
    prefix="/meals",
    tags=["meals"],
    # always verify the JWT token
    dependencies=[Depends(auth.verify_token)],
)


@router.get("")
async def list_meals(db:Client = Depends(auth.get_supabase_client)):
    response = db.schema("app").table("meals").select("*").execute()
    return response.data
