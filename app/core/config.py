# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Charge .env et ignore les variables inconnues
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Valeurs par défaut (pas "required")
    app_name: str = "Auth Service API"
    env: str = "dev"
    host: str = "0.0.0.0"
    port: int = 8000
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Required (doivent venir du .env)
    database_url: str  # lit DATABASE_URL
    jwt_secret: str    # lit JWT_SECRET

settings = Settings()