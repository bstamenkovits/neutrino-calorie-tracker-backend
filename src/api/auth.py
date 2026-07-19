from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core import auth

router = APIRouter(tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


@router.post("/login")
async def login(credentials: LoginRequest) -> LoginResponse:
    session = auth.log_in(credentials.email, credentials.password)

    if session is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return LoginResponse(
        access_token=session.access_token,
        refresh_token=session.refresh_token,
        token_type="bearer",
    )
