import React, { useState, useEffect } from "react";
import WeatherForm from "./components/WeatherForm";
import WeatherDisplay from "./components/WeatherDisplay";
import HistoryList from "./components/HistoryList";
import axios from "./axiosConfig";
import type { WeatherData, HistoryItem, ErrorItem } from "./types";

const App: React.FC = () => {
  const [weather, setWeather] = useState<WeatherData | ErrorItem | null>(null);
  const [history, setHistory] = useState<HistoryItem[]>([]);

  const fetchWeather = async (city: string) => {
    try {
      const response = await axios.get<WeatherData | ErrorItem>(
        `/weather?city=${city}`
      );
      if ("error" in response.data) {
        alert(response.data.error);
        setWeather(null);
      } else {
        setWeather(response.data);
        loadHistory();
      }
    } catch (error) {
      console.log(error);
      alert("Error with fetching weather data");
    }
  };

  const loadHistory = async () => {
    const response = await axios.get<HistoryItem[]>("/history");
    setHistory(response.data);
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Current Weather by City</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <WeatherForm onSearch={fetchWeather} />
          {weather && <WeatherDisplay data={weather} />}
        </div>
        <div>
          <h2 className="text-xl font-semibold mb-2">Query History</h2>
          <HistoryList history={history} onSelect={fetchWeather} />
        </div>
      </div>
    </div>
  );
};

export default App;
