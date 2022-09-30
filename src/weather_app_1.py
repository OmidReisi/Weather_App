import os

import requests
from dotenv import load_dotenv

load_dotenv(r"./api/weather_api.env")

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"


response = requests.get(request_url, timeout=7)

if not response.ok:
    raise requests.ConnectionError("CITY NOT FOUND")

data = response.json()
weather = data["weather"][0]["description"]
temp = data["main"]["temp"] - 273.15

print(f"{city.capitalize()}: {temp:.2f} °C, {weather}")
