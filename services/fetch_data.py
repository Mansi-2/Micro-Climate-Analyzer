import requests
import pandas as pd
from utils.database import get_connection

LAT = 22.7196   # For Indore
LON = 75.8577

def fetch_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=temperature_2m_max,relative_humidity_2m_max,windspeed_10m_max&timezone=auto"
    res = requests.get(url).json()

    df = pd.DataFrame({
        "date": res["daily"]["time"],
        "temperature": res["daily"]["temperature_2m_max"],
        "humidity": res["daily"]["relative_humidity_2m_max"],
        "windspeed": res["daily"]["windspeed_10m_max"]
    })

    return df


def fetch_aqi():
    url = f"https://api.openaq.org/v2/latest?coordinates={LAT},{LON}&radius=10000"
    res = requests.get(url).json()

    try:
        aqi = res["results"][0]["measurements"][0]["value"]
    except:
        aqi = None

    return aqi


def store_data():
    df = fetch_weather()
    aqi = fetch_aqi()
    df["aqi"] = aqi

    conn = get_connection()
    df.to_sql("climate_data", conn, if_exists="replace", index=False)
    conn.close()