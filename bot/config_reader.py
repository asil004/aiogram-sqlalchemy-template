from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_URL: str
    ADMINS: list[int]
    CODE: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
