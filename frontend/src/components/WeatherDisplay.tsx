import React from "react";
import type { ErrorItem, WeatherData } from "../types";

interface DataProps {
  data: WeatherData | ErrorItem;
}

const WeatherDisplay: React.FC<DataProps> = ({ data }) => {
  if ("error" in data) {
    return (
      <div className="border p-4 rounded text-red-500">Error: {data.error}</div>
    );
  }

  return (
    <div className="border p-4 rounded space-y-2">
      <p>Temperature: {data.temp}°C</p>
      <p>Feels like: {data.feels_like}°C</p>
      <p>
        Min: {data.temp_min}°C, Max: {data.temp_max}°C
      </p>
      <p>Wind speed: {data.wind_speed} m/s</p>
      <p>Description: {data.weather_description}</p>
    </div>
  );
};

export default WeatherDisplay;
