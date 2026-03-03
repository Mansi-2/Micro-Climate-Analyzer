import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df):
    corr = df.select_dtypes(include="number").corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Micro-Climate Correlation Heatmap")
    return plt


def plot_timeseries(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["date"], df["temperature"], label="Temp")
    plt.plot(df["date"], df["aqi"], label="AQI")
    plt.legend()
    plt.title("Temperature & AQI Over Time")
    return plt