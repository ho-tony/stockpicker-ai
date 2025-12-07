from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "StockPicker AI Backend"
    GEMINI_API_KEY: str
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    USE_MOCK_SERVICE: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
