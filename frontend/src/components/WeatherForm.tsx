import React, { useState } from "react";

interface WeatherProps {
  onSearch: (city: string) => void;
}

const WeatherForm: React.FC<WeatherProps> = ({ onSearch }) => {
  const [city, setCity] = useState("");

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (city.trim()) {
      onSearch(city.trim());
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
      <input
        type="text"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        placeholder="Enter city"
        className="border p-2 flex-grow rounded"
      />
      <button type="submit" className="bg-blue-500 text-white px-4 rounded">
        Search
      </button>
    </form>
  );
};

export default WeatherForm;
