from pathlib import Path
from os import getenv, path
from dotenv import load_dotenv
from .base import *
from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)



# python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = getenv("DJANGO_SECRETE_KEY",)

ADMIN_URL = getenv("DJANGO_ADMIN_URL")

ALLOWED_HOSTS = []


ADMINS = [("Eng AKS", "engaks826@gmail.com"),]