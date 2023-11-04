from functools import lru_cache

from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    OTP_ORIGIN_NUMBER: str
    DATABASE_CONNECTION_STRING: str
    AWS_REGION_NAME: str
    AWS_ACCESS_KEY: str
    AWS_PRIVATE_KEY: str
    AWS_APPLICATION_ID: str

    JWT_SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
