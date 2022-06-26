import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file: str = '.env'