import React from "react";
import type { HistoryItem } from "../types";

interface HistoryProps {
  history: HistoryItem[];
  onSelect: (city: string) => void;
}

const HistoryList: React.FC<HistoryProps> = ({ history, onSelect }) => (
  <ul className="border p-4 rounded space-y-2 max-h-80 overflow-auto">
    {history.map((item) => (
      <li
        key={item.id}
        className="cursor-pointer hover:bg-gray-100 p-2 rounded"
        onClick={() => onSelect(item.city)}
      >
        <strong>{item.city}</strong> — {item.temp}°C
      </li>
    ))}
  </ul>
);

export default HistoryList;
