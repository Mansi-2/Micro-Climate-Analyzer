import streamlit as st
from services.fetch_data import store_data
from services.process_data import load_data, engineer_features
from services.anomaly import compute_zscore, cusum_detection
from services.visualize import plot_heatmap, plot_timeseries
from utils.database import create_table

st.title("Micro-Climate Analyzer")

create_table()

if st.button("Fetch Latest Data"):
    store_data()
    st.success("Data Updated!")

df = load_data()
df = engineer_features(df)
df = compute_zscore(df, "aqi")
df = cusum_detection(df, "aqi")

st.write("Data Preview")
st.dataframe(df.tail())

st.pyplot(plot_timeseries(df))
st.pyplot(plot_heatmap(df))

st.write("Anomalies Detected")
st.dataframe(df[df["aqi_anomaly"] == True])