from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db_handler import DatabaseHandler
from app.services.weather_api import get_city_weather
from app.services.functions import get_specific_data
from app.models.pd_models import WeatherDetailsModel
from app.core.logger import logger


app = FastAPI()
db = DatabaseHandler()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"msg": "There are test message."}


@app.get("/weather")
def get_weather_point(city: str | None = None):
    logger.info(f"GET /weather called with city: {city}")
    if city:
        weather_data = get_city_weather(city)
        if isinstance(weather_data, WeatherDetailsModel):
            logger.info(f"Weather data fetched successfully for city: {city}")
            db.add_new_query(city_name=city, weather_details=weather_data)
            return weather_data.model_dump()
        else:
            logger.warning(
                f"Failed to fetch weather data for city '{city}': {weather_data.message}")
            return {'error': weather_data.message}


@app.get("/history")
def get_history_point():
    logger.info("GET /history called")
    recent_queries = db.get_query_history()
    history = [get_specific_data(x) for x in recent_queries]

    logger.info(f"Returned {len(history)} historical records")
    return history
