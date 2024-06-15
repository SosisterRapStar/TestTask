from pydantic_settings import BaseSettings
from pydantic import Field

class DbSettings(BaseSettings):
    pass




class DBSettings(BaseSettings):
    db_string_url: str = Field(env='DB_STRING_URL')
    db_user: str = Field(default='user', env='DB_USER')
    db_password: str = Field(default='1234', env='DB_PASSWORD')
    db_host: str = Field(default='localhost',env='DB_HOST')
    db_port: int = Field(default=5432, env='DB_PORT')
    db_name: str = Field(default='postgres', env='DB_NAME')
    

class Settings(BaseSettings):
    db = DBSettings()


settings = Settings()
 