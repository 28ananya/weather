# backend/services/rollups.py

import pandas as pd
from data.database import store_daily_summary

# Function to calculate daily aggregates
def calculate_daily_aggregates(weather_data):
    df = pd.DataFrame(weather_data)
    daily_aggregates = df.groupby('city').agg({
        'temp': ['mean', 'max', 'min'],
        'main': lambda x: x.mode()[0]  # Most frequent weather condition
    }).reset_index()

    daily_aggregates.columns = ['city', 'avg_temp', 'max_temp', 'min_temp', 'dominant_weather']
    for _, row in daily_aggregates.iterrows():
        store_daily_summary(
            city=row['city'],
            date=pd.Timestamp.now().strftime('%Y-%m-%d'),
            avg_temp=row['avg_temp'],
            max_temp=row['max_temp'],
            min_temp=row['min_temp'],
            dominant_weather=row['dominant_weather']
        )
