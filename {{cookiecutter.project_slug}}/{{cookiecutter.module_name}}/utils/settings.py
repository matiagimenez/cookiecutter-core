from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    TEST_SETTING: str = Field(
        default="TEST_SETTING",
        description="Test setting",
    )


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()


Settings = get_settings()
