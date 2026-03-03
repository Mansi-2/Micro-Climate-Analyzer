import pandas as pd
from utils.database import get_connection

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM climate_data", conn)
    conn.close()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df


def engineer_features(df):

    # Humidity Index
    df["humidity_index"] = df["temperature"] * df["humidity"] / 100

    # Pollution Density
    df["pollution_density"] = df["aqi"] / (df["windspeed"] + 1)

    # Heat Stress Level
    df["heat_stress"] = df["temperature"] + (0.33 * df["humidity"]) - (0.7 * df["windspeed"])

    return df