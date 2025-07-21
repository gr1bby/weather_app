export interface WeatherData {
  temp: number;
  feels_like: number;
  temp_min: number;
  temp_max: number;
  wind_speed: number;
  weather_description: string;
}

export interface HistoryItem {
  id: number;
  city: string;
  temp: number;
  timestamp: string;
}

export interface ErrorItem {
  error: string;
}
