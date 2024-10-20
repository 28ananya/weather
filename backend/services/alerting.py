# backend/services/alerting.py

from config.settings import ALERT_THRESHOLD_TEMP

def check_alerts(weather_data):
    for data in weather_data:
        if data['temp'] > ALERT_THRESHOLD_TEMP:
            print(f"Alert: Temperature in {data['city']} exceeds {ALERT_THRESHOLD_TEMP}°C!")
