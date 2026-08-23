import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MAX_MODEL = os.getenv("MAX_MODEL", "openrouter/free")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set.")