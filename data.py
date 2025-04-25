import sqlite3
from sqlite3 import connect
import csv
import os
from datetime import datetime

# Ensure cross-platform file paths
db_path = os.path.join("database", "weatherincity.db")
# Create connection
conn = sqlite3.connect(db_path)

def create_table():
    # start navigation to DB
    nav = conn.cursor()
    # execute the code
    nav.execute("""
        CREATE TABLE IF NOT EXISTS weather_city 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            windspeed REAL,
            longitude REAL,
            latitude REAL,
            city TEXT,
            country TEXT, 
            timestamp TEXT
        )
                """
                )
    conn.commit()
    conn.close()

def insert_weather_data(temperature, windspeed, longitude, latitude, city, country):
    conn = sqlite3.connect(db_path)
    nav = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nav.execute("""
        INSERT INTO weather_city (temperature, windspeed, longitude, latitude, city, country, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (temperature, windspeed, longitude, latitude, city, country, timestamp))
    conn.commit()
    conn.close()

def export_to_csv():
    nav = conn.cursor()
    nav.execute("SELECT * FROM company_data")

    conn.commit()
    conn.close()

    for row in nav.fetchall():
        print(row)