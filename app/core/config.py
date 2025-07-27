from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    gemini_key: str

    model_config = ConfigDict()
    model_config["env_file"] = ".env"

settings = Settings()