"""
This module provides authentication-related functionality.

The general flow is as follows:

            Authorization header
                    ↓
                get_token()
                    ↓
               verify_token()
            ↙                ↘
get_current_user()      get_supabase_client()
"""

import os
from dataclasses import dataclass
from typing import Any

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_PUBLISHABLE_KEY = os.environ.get("SUPABASE_PUBLISHABLE_KEY", "")

_jwks_client = jwt.PyJWKClient(
    f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json",
    cache_keys=True,
)


bearer_scheme = HTTPBearer(auto_error=False)


def get_token(creds: HTTPAuthorizationCredentials | None = Depends(bearer_scheme)) -> str:
    """
    Retrieve the token from the Authorization header.

    Args:
        creds: the credentials from the Authorization header

    Returns:
        access_token: the access token taken from the header

    """
    if not creds:
        raise HTTPException(401, "Missing bearer token")

    access_token = creds.credentials
    return access_token


def verify_token(access_token: str = Depends(get_token)) -> dict[str, Any]:
    """
    Access token is verified by decoding it with the public key from the JWKS endpoint.

    If the token is missing, invalid, or expired, an HTTPException is raised. jwt.decode() will
    raise a PyJWTError if the token is invalid.

    Args:
        access_token: the access token taken from the header

    Returns:
        verified_claims: the claims from the verified token
    """
    try:
        signing_key = _jwks_client.get_signing_key_from_jwt(access_token)
        verified_claims = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=["ES256"],
            audience="authenticated",
        )
        return verified_claims
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid or expired token")


@dataclass
class UserData:
    user_id: str
    email: str
    role: str


def get_user_data(verified_claims: dict[str, Any] = Depends(verify_token)) -> UserData:
    """
    Extract the user data from the verified claims.

    Args:
        verified_claims: the claims from the verified token

    Returns:
        UserData: the user data
    """
    return UserData(
        user_id=verified_claims["sub"],
        email=verified_claims["email"],
        role=verified_claims["role"],
    )

def get_supabase_client(
        access_token: str = Depends(get_token),
        _verified: dict[str, Any] = Depends(verify_token),
) -> Client:
    """
    Construct a Supabase client with the given access token.

    The `verify_token` dependency is used to make sure the token is valid, the content of said token
    is not explicitly used.

    The `create_client` function is used to create a public client, giving the client access to all tables
    that the `anon` role has access to. RLS is applied to each table in the database. All tables have a RLS
    policy that only gives access to `authenticated` role. Some tables have RLS policies that restrict the
    user to only see their own rows.

    Args:
        access_token: the access token taken from the header
        _verified: the claims from the verified token

    Returns:
        Client: the Supabase client
    """
    # public/anonymous client
    client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)

    # assign `authenticated` role to the client
    client.postgrest.auth(access_token)

    return client


def login(email, password):
    # public/anonymous client
    client = create_client(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY)
    return client.auth.sign_in_with_password(dict(email=email, password=password)).session

