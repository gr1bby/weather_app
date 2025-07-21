import requests
from pydantic import ValidationError

from app.core.config import OPEN_WEATHER_API_BASE_URL, settings
from app.core.logger import logger
from app.models.pd_models import GetCityWeatherResponseModel, WeatherDetailsModel, ErrorResponseModel


def get_city_weather(city_name: str) -> WeatherDetailsModel | ErrorResponseModel:
    """
    Get city weather with using OpenWeatherAPI.

    Args:
        city_name (str): City name.

    Returns:
        WeatherDetailsModel | ErrorResponseModel: If city name incorrect will raising `ErrorResponseModel`.
    """
    
    logger.info(f"Fetching weather for city: {city_name}")
    params = {
        "q": city_name,
        'units': 'metric',
        "appid": settings.WEATHER_API_KEY
    }
    response = requests.get(OPEN_WEATHER_API_BASE_URL, params=params)
    logger.debug(f"External API response status: {response.status_code}")
    
    if response.status_code == 200:
        response_data = response.json()
        validated_data = GetCityWeatherResponseModel.model_validate(response_data, by_alias=True)
        final_data = WeatherDetailsModel(
            temp=validated_data.main.temp,
            feels_like=validated_data.main.feels_like,
            temp_min=validated_data.main.temp_min,
            temp_max=validated_data.main.temp_max,
            wind_speed=validated_data.wind.speed,
            weather_description=validated_data.weather[0].description
        )
        
        logger.info(f"Successfully fetched weather for {city_name}")
        return final_data

    elif response.status_code == 404:
        logger.warning(f"City not found: {city_name}")
        return ErrorResponseModel.model_validate(response.json())
    
    else:
        logger.error(f"Unexpected status {response.status_code} for city '{city_name}'")
        return ErrorResponseModel(cod="404", message="Unexpected error occurred")
