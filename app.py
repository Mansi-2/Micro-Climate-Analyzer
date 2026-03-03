import streamlit as st
from services.fetch_data import store_data
from services.process_data import load_data, engineer_features
from services.visualize import plot_heatmap, plot_timeseries
from utils.database import create_table
from services.anomaly import detect_trend_anomalies

st.title("Micro-Climate Analyzer")

create_table()

if st.button("Fetch Latest Data"):
    store_data()
    st.success("Data Updated!")

df = load_data()
df = df.dropna(subset=["aqi"])
df = engineer_features(df)
df = detect_trend_anomalies(df)

st.write("Data Preview")
st.dataframe(df.tail())

st.pyplot(plot_timeseries(df))
st.pyplot(plot_heatmap(df))


st.subheader("AQI Trend Analysis")

# Line chart
st.line_chart(df.set_index("date")[["aqi", "rolling_mean"]])

# Extract anomalies
trend_anomalies = df[df["trend_anomaly"] == True]

if trend_anomalies.empty:
    st.success("No sudden AQI trend shifts detected in this period.")
else:
    st.error("Sudden AQI trend shifts detected!")
    st.dataframe(trend_anomalies[["date", "aqi", "aqi_change"]])