import os
from supabase import create_client, Client
# from dotenv import load_dotenv

# load_dotenv()
from dotenv import load_dotenv, find_dotenv

# Forces the script to locate the file, regardless of PyCharm's execution directory
load_dotenv(find_dotenv(usecwd=False))


supabase_client: Client = create_client(
    os.environ.get("SUPABASE_URL", ""),
    os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
)
