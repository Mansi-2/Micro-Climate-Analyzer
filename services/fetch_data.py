import requests
import pandas as pd
from datetime import datetime, timedelta
from utils.database import get_connection

LAT = 22.7196   # Indore
LON = 75.8577


def fetch_weather():
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=30)

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LAT}&longitude={LON}"
        f"&daily=temperature_2m_max,relative_humidity_2m_max,windspeed_10m_max"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&timezone=auto"
    )

    res = requests.get(url).json()

    if "daily" not in res:
        print("Weather API Error:", res)
        return pd.DataFrame()

    df = pd.DataFrame({
        "date": res["daily"]["time"],
        "temperature": res["daily"]["temperature_2m_max"],
        "humidity": res["daily"]["relative_humidity_2m_max"],
        "windspeed": res["daily"]["windspeed_10m_max"]
    })

    return df


def fetch_aqi():
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=6)

    url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality?"
        f"latitude={LAT}&longitude={LON}"
        f"&hourly=pm2_5"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&timezone=auto"
    )

    res = requests.get(url).json()

    if "hourly" not in res:
        print("AQI API Error:", res)
        return pd.DataFrame()

    df = pd.DataFrame({
        "datetime": res["hourly"]["time"],
        "pm2_5": res["hourly"]["pm2_5"]
    })

    # Convert to datetime
    df["datetime"] = pd.to_datetime(df["datetime"])

    # Extract date
    df["date"] = df["datetime"].dt.date

    # Daily average PM2.5
    daily_df = df.groupby("date")["pm2_5"].mean().reset_index()
    daily_df.rename(columns={"pm2_5": "aqi"}, inplace=True)

    return daily_df


def store_data():
    print("Fetching weather data...")
    weather_df = fetch_weather()

    print("Fetching AQI data...")
    aqi_df = fetch_aqi()

    if weather_df.empty or aqi_df.empty:
        print("One of the datasets is empty.")
        return

    # Ensure same date type before merge
    weather_df["date"] = pd.to_datetime(weather_df["date"]).dt.date
    aqi_df["date"] = pd.to_datetime(aqi_df["date"]).dt.date

    # Merge on date
    df = pd.merge(weather_df, aqi_df, on="date")

    if df.empty:
        print("Merge failed. No matching dates.")
        return

    print("Merged DF:")
    print(df.head())

    conn = get_connection()
    df.to_sql("climate_data", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    print("Stored rows:", len(df))