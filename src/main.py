import uvicorn
import jwt
from fastapi import FastAPI, Header, HTTPException
from supabase import AuthApiError, PostgrestAPIError

from core.database.client import verify_access_token

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/meals")
async def list_meals(authorization:str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing bearer token")
    token = authorization.removeprefix("Bearer ")
    try:
        claims = verify_access_token(token)  # raises on bad sig / expired
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid or expired token")

    # client = create_user_client(token)
    # response = client.schema("app").table("meals").select("*").execute()
    # return response.data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)


