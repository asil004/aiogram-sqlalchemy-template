from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     bot_token: SecretStr
#     db_url: PostgresDsn
#
#     # class Config:
#     #     env_file = '.env'
#     #     env_file_encoding = 'utf-8'
#     model_config = SettingsConfigDict(env_file='.env')
#
#
# config = Settings()
