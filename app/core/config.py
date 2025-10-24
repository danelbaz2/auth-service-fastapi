from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Auth Service API"
    env: str = "dev"
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()