from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DefaultDBSettings(BaseSettings):
    engine: str = 'django.db.backends.postgresql'
    host: str = Field(min_length=1)
    port: int = Field(gt=0)
    user: str = Field(min_length=1, validation_alias='default_db_user')
    password: str = Field(validation_alias='default_db_pass')
    name: str = Field(min_length=1)

    model_config = SettingsConfigDict(env_prefix='default_db_')
