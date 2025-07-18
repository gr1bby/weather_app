from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func

from app.database.db_config import db_config


class WeatherQueryDetails(db_config.Base):
    """
    Model for weather query details.
    
    Consists of:
        id (int): ID of query. PK.
        city_name (str): City name.
        query_timestamp (DateTime): Time of query creating. Autocreating.
        weather_details (JSON): JSON object which including weather data (temperature, weather description, etc.)
    """
    __tablename__ = 'weather_details'
    
    id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=False)
    query_timestamp = Column(DateTime, default=func.now())
    weather_details = Column(JSON, nullable=False)
    
    def __repr__(self) -> str:
        return (
            f"<WeatherQueryDetails(id={self.id}, "
            f"city_name={self.city_name}, "
            f"query_timestamp={self.query_timestamp})>"
        )
