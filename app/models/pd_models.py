from pydantic import BaseModel


class DB_WeatherDetailsJSON(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    wind_speed: float
    weather_description: str
