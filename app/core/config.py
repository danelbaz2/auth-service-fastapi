from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.app", extra="ignore")

    app_name: str = Field(..., alias="APP_NAME")
    env: str = Field(..., alias="ENV")
    host: str = Field(..., alias="HOST")
    port: int = Field(..., alias="PORT")
    jwt_algorithm: str = Field(..., alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(..., alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    database_url: str = Field(..., alias="DATABASE_URL")
    jwt_secret: str = Field(..., alias="JWT_SECRET")

settings = Settings()
