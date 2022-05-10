from pydantic import BaseSettings, Field
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class AppSettings(BaseSettings):
    URL_ETERSCAN: str = "https://api.etherscan.io/api"
    API_KEY: str

@lru_cache()
def get_settings():
    return AppSettings()