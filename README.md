# Micro-Climate Analyzer

A data science project that detects micro-climate anomalies by combining weather data and air pollution metrics.

Instead of predicting weather, this system analyzes environmental patterns to identify unusual atmospheric behavior using statistical control techniques.

---

## Project Overview

This project collects real-time environmental data from public APIs and performs:

- Time-series analysis  
- Feature engineering  
- Rolling Z-score anomaly detection  
- CUSUM drift detection  
- Correlation heatmap analysis  
- Interactive dashboard visualization  

The goal is to detect abnormal micro-climate behavior such as sudden pollution spikes, unusual humidity interactions, or sustained environmental drift.

---

## Data Sources

- Open-Meteo API (Weather Data)  
- OpenAQ API (Air Quality Data)  

All data is dynamically fetched from live APIs. No static datasets are used.

---

## Engineered Features

- Humidity Index  
- Pollution Density  
- Heat Stress Level  

These derived variables help analyze environmental stress patterns beyond raw values.

---

## Anomaly Detection Techniques

### Rolling Z-Score

Uses rolling mean and standard deviation to detect short-term anomalies.

**Condition Used:**  
Absolute Z-score > 2.5 → flagged as anomaly

---

### CUSUM (Cumulative Sum Control Chart)

Detects gradual long-term drift in pollution levels.

This helps identify structural environmental shifts instead of just single-day spikes.

---

## Visualizations

- Micro-climate correlation heatmap  
- Temperature & AQI time-series plot  
- Anomaly flagged dataset view  
- Pollution vs weather relationship analysis  

All visualizations are available through a Streamlit dashboard.

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- SQLite  
- Streamlit  

---


---

## Why This Project Stands Out

Most beginner projects focus on prediction.

This project focuses on statistical environmental behavior analysis using live API ingestion, feature engineering, control chart methods, and time-series exploration.

It demonstrates applied data science beyond basic machine learning tutorials.

---

## Future Improvements

- Multi-city comparison  
- Trend decomposition using Prophet  
- Clustering anomaly types  
- Automated daily scheduled data updates  
- Advanced anomaly explanation module  

---
 
