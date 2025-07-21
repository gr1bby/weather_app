from app.models.pd_models import QueryHistoryModel
from app.models.db_models import WeatherQueryDetails


def get_specific_data(data: WeatherQueryDetails) -> dict:
    """
    Getting some data from db row for sending to frontend.

    Args:
        data (WeatherQueryDetails): Object from DB.

    Returns:
        dict: QueryHistoryModel looking dictionary.
    """
    right_datamodel = QueryHistoryModel(
        id=data.id,
        city=data.city_name,
        temp=data.weather_details['temp'],
        timestamp=data.query_timestamp.strftime("%Y-%m-%d %H:%M:%S")
    )
    return right_datamodel.model_dump()
