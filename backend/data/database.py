# backend/data/database.py

import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                      city TEXT, 
                      date TEXT, 
                      avg_temp REAL, 
                      max_temp REAL, 
                      min_temp REAL, 
                      dominant_weather TEXT)''')
    conn.commit()
    conn.close()

def store_daily_summary(city, date, avg_temp, max_temp, min_temp, dominant_weather):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_weather)
                      VALUES (?, ?, ?, ?, ?, ?)''', (city, date, avg_temp, max_temp, min_temp, dominant_weather))
    conn.commit()
    conn.close()
