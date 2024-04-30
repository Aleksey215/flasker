"""
App settings validation and management
"""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """
    Get env vars for using in app settings

    Args:
        BaseSettings (_type_): pydantic class
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )

    SECRET_KEY: str = Field(min_length=5)


settings = AppConfig().model_dump()
