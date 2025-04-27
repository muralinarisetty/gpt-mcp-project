import requests

MCP_SERVER_URL = "http://localhost:5000"

def get_weather(city: str, unit: str = "celsius") -> str:
    response = requests.post(f"{MCP_SERVER_URL}/weather", json={"city": city, "unit": unit})
    response.raise_for_status()
    return response.json().get("weather_report", "No weather report available.")