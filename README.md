# Bike Demand Forecasting Using ARIMA (Hourly)

This project is part of my AICTE Virtual Internship, where I built a time-series forecasting model to predict hourly bike rental demand using the ARIMA model. The goal was to analyze historical rental patterns and make accurate short-term forecasts to help with resource planning in a bike-sharing system.

---

## Problem Statement

Bike-sharing systems often struggle with predicting demand on an hourly basis. Accurately forecasting how many bikes will be needed can help reduce shortages or idle resources. This project focuses on predicting the number of bike rentals for the next hour using historical data.

---

## Dataset

- **Source**: [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)
- **File Used**: `hour.csv`
- This file contains hourly rental data with features like date, season, temperature, humidity, and the total count (`cnt`) of bikes rented.

For this project, I focused on using the `cnt` column to train a univariate ARIMA model.

---

## Model Overview

I used the ARIMA (AutoRegressive Integrated Moving Average) model from the `statsmodels` library to forecast future values based on past rental data.

### Why ARIMA?
- It works well for univariate time series
- Doesn’t require external variables
- Easy to train and deploy
- Offers good baseline accuracy for structured temporal data

---

## Implementation

I used Jupyter Notebook (or Google Colab) to experiment with the dataset, visualize the trends, and build the forecasting model.

Key steps:
- Load and clean the `hour.csv` data
- Check stationarity and perform differencing
- Fit ARIMA with selected parameters (e.g. (3,1,2))
- Forecast the next value
- Evaluate using MAE and RMSE

After training, I saved the model as `arima_bike_model.pkl` using `joblib`.

---

## Requirements

Install the necessary libraries with:

```bash
pip install flask joblib pandas statsmodels matplotlib seaborn scikit-learn
