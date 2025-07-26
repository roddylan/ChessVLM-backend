from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gemini_key: str

    class Config:
        env_file = '.env'

settings = Settings()