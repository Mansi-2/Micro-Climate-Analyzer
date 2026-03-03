import pandas as pd

def detect_trend_anomalies(df, column="aqi", change_threshold=15):
    df = df.copy()

    # Daily change
    df["aqi_change"] = df[column].diff()

    # Rolling mean (7-day trend)
    df["rolling_mean"] = df[column].rolling(window=7).mean()

    # Deviation from rolling trend
    df["trend_deviation"] = df[column] - df["rolling_mean"]

    # Sudden jump detection
    df["trend_anomaly"] = df["aqi_change"].abs() > change_threshold

    return df