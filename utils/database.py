import sqlite3
import os

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect("data/climate.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS climate_data (
                   date TEXT PRIMARY KEY,
                   temperature REAL,
                   humidity REAL, 
                   windspeed REAL,
                   aqi REAL)
                   """)
    conn.commit()
    conn.close()