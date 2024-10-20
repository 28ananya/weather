# backend/services/weather_api.py

import requests
from config.settings import API_KEY, BASE_URL

# Function to fetch weather data for a specific city
def fetch_weather_data(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json()['message']}")
        return None

# Kelvin to Celsius conversion
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15
