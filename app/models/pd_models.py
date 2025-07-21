from typing import List, Dict, Optional
from pydantic import BaseModel, Field, model_validator, ValidationError


class WeatherDetailsModel(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    wind_speed: float
    weather_description: str


# ------------------Weather Response inner models---------------------

class CoordModel(BaseModel):
    lon: float
    lat: float
    
class WeatherModel(BaseModel):
    id: int
    main: str
    description: str
    icon: str
    
class MainModel(BaseModel):
    temp: float
    feels_like: float 
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int
    
class WindModel(BaseModel):
    speed: float
    deg: int
    gust: Optional[float] = None
    
class CloudsModel(BaseModel):
    all: int
    
class RainModel(BaseModel):
    one_hour: float = Field(None, alias="1h")
    
class SnowModel(BaseModel):
    one_hour: float = Field(None, alias="1h")
    
class SysModel(BaseModel):
    type: Optional[int] = None
    id: Optional[int] = None
    message: Optional[float] = None
    country: str
    sunrise: int
    sunset: int
    
# --------------------------------------------------------------

class GetCityWeatherResponseModel(BaseModel):
    coord: CoordModel
    weather: List[WeatherModel]
    base: str
    main: MainModel
    visibility: int
    wind: WindModel
    clouds: CloudsModel
    rain: Optional[RainModel] = None
    snow: Optional[RainModel] = None
    dt: int
    sys: SysModel
    timezone: int
    id: int
    name: str
    cod: int | str
    
    # @model_validator(mode='before')
    # def validate_404_error(cls, values):
    #     if values['cod'] == "404":
    #         raise ValidationError("City not found.")
    #     return values


class ErrorResponseModel(BaseModel):
    cod: str
    message: str
    

class QueryHistoryModel(BaseModel):
    id: int
    city: str
    temp: float
    timestamp: str
