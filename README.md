# Weather App

A fullstack application which showing current weather and query history.
Frontend built with React.ts (Vite), TailwindCSS and Axios.
Backend built with FastAPI and PostgreSQL using openweathermap.org.

## Setup

1. **Clone & enter project**  
    ```bash
    git clone https://github.com/your-username/weather_app.git
    cd weather_app


Create .env (in the project root)

DB_HOST=host
DB_PORT=port 
DB_USER=username
DB_PASS=password
DB_NAME=db_name
WEATHER_API_KEY=your_openweather_api_key


Install & run backend

cd app
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows PowerShell:
venv\Scripts\Activate.ps1

pip install -r ../requirements.txt
uvicorn app.main:app --reload --port 8000

Open API docs at http://localhost:8000/docs.

Install & run frontend

cd frontend
npm install
npm run dev

Visit http://localhost:5173.

With Docker

If you have Docker and Docker Compose:

docker-compose build
docker-compose up

Backend: http://localhost:8000
Frontend: http://localhost:5173


# How to Use

Type a city name and click Search.
See current weather and a history of recent searches.
Click a past city to get current weather of the city.
