import numpy as np
import pandas as pd

def compute_zscore(df, column):
    rolling_mean = df[column].rolling(window=5).mean()
    rolling_std = df[column].rolling(window=5).std()

    df[f"{column}_z"] = (df[column] - rolling_mean) / rolling_std
    df[f"{column}_anomaly"] = df[f"{column}_z"].abs() > 2.5
    return df


def cusum_detection(df, column, threshold=5):
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=[column])
    mean = df[column].mean()
    pos_cusum = [0]
    neg_cusum = [0]

    for x in df[column]:
        pos_cusum.append(max(0, pos_cusum[-1] + x - mean))
        neg_cusum.append(min(0, neg_cusum[-1] + x - mean))

    df["cusum_positive"] = pos_cusum[1:]
    df["cusum_negative"] = neg_cusum[1:]
    df["cusum_anomaly"] = (df["cusum_positive"] > threshold) | (df["cusum_negative"] < -threshold)

    return df