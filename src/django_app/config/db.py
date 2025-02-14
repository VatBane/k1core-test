from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DefaultDBSettings(BaseSettings):
    ENGINE: str = 'django.db.backends.postgresql'
    HOST: str = Field(min_length=1)
    PORT: int = Field(gt=0)
    USER: str = Field(min_length=1, validation_alias='DEFAULT_DB_USER')
    PASSWORD: str = Field(validation_alias='DEFAULT_DB_PASS')
    NAME: str = Field(min_length=1)

    model_config = SettingsConfigDict(env_prefix='DEFAULT_DB_')
