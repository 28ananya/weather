# backend/app.py

from flask import Flask, jsonify, render_template
import pandas as pd
from services.weather_api import fetch_weather_data, kelvin_to_celsius
from services.rollsup import calculate_daily_aggregates
from services.alerting import check_alerts
from config.settings import CITIES

app = Flask(__name__)

# Simulated weather data fetching
def get_weather_data():
    weather_data = []
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data.append({
                'city': city,
                'main': data['weather'][0]['main'],
                'temp': kelvin_to_celsius(data['main']['temp']),
                'feels_like': kelvin_to_celsius(data['main']['feels_like']),
                'timestamp': data['dt']
            })
    return weather_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def weather():
    weather_data = get_weather_data()
    # Aggregates and alerts (daily summary calculation and alerting)
    calculate_daily_aggregates(weather_data)
    check_alerts(weather_data)

    # Return the full data as JSON
    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

