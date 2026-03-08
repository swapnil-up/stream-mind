from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field

class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(...)
    DATABASE_URL: str = Field(...)
    JWT_SECRET_KEY: str = Field(...)
    JWT_ALGORITHM: str = Field(...)
    JWT_EXPIRE_MINUTES: int = Field(...)
    BACKEND_CORS_ORIGINS: List[str] = Field(...)

    model_config = SettingsConfigDict(env_file="../.env")

settings = Settings()
