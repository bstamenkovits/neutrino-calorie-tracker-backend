import os
import jwt
from typing import Any
from supabase import create_client, Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=False))


SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_JWT_SECRET_KEY = os.environ.get("SUPABASE_JWT_SECRET_KEY", "")
SUPABASE_SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
SECRET_KEY = os.environ.get("SUPABASE_JWT_SECRET_KEY", "")

_jwks_client = jwt.PyJWKClient(
    f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json",
    cache_keys=True,
)
supabase_client_admin: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)


def log_in(email:str, password:str) -> Any:
    client = create_client(
        os.environ.get("SUPABASE_URL", ""),
        os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    )
    response = client.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })
    return response.session


def verify_access_token(access_token: str) ->  dict[str, Any]:
    signing_key = _jwks_client.get_signing_key_from_jwt(access_token)
    return jwt.decode(
        access_token,
        signing_key.key,
        algorithms=["ES256"],
        audience="authenticated",
    )

