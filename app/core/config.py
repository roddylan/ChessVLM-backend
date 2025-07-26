from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gemini_key: str



settings = Settings()