from typing import List

from app.models.db_models import WeatherQueryDetails
from app.models.pd_models import DB_WeatherDetailsJSON
from db_setup import DatabaseSetup


class DatabaseHandler:
    def __init__(self):
        """
        Initialize DatabaseHandler object.
        Creating of engine, session and tables.
        """
        db_setup = DatabaseSetup()
        __engine = db_setup.create_engine()
        db_setup.create_tables(__engine)
        self.__session = db_setup.create_session(__engine)
        
        
    def add_new_query(self, city_name: str, weather_details: DB_WeatherDetailsJSON) -> WeatherQueryDetails:
        """
        Add new query to database.

        Args:
            city_name (str): City name.
            weather_details (DB_WeatherDetailsJSON): JSON looking object with weather details.

        Returns:
            WeatherQueryDetails: WeatherQueryDetails object.
        """
        new_query = WeatherQueryDetails(
            city_name=city_name,
            weather_details=weather_details.model_dump()
        )
        self.__session.add(new_query)
        self.__session.commit()
        return new_query
    
    
    def get_query_history(self, query_count: int | None = None) -> List[WeatherQueryDetails]:
        """
        Return query history. If specified `query_count` it will show only this number of recent queries.

        Args:
            query_count (int | None, optional): Count of recent queries which need to show. Defaults to None (all queries).

        Returns:
            List[WeatherQueryDetails]: List of queries.
        """
        return self.__session.query(WeatherQueryDetails).order_by(WeatherQueryDetails.id.desc()).limit(query_count).all()
    
