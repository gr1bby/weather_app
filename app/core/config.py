from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    WEATHER_API_KEY: str


settings = Settings()

OPEN_WEATHER_API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
