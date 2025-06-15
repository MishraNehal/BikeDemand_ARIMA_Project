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

The ARIMA model is trained dynamically during each prediction using the latest data from `hour.csv`.

---

## Requirements

Install the necessary libraries with:

```bash
pip install flask joblib pandas statsmodels matplotlib seaborn scikit-learn gunicorn
```

--- 

## Local Deployment

1. Clone the repository and ensure `hour.csv` is present in the root folder for live model training
2. Run the Flask app:
```bash
python app.py
```

3. Open your browser and go to:
```
http://127.0.0.1:5000
```

Click “Predict” to get the next hour's demand forecast.

---

## Deployment on Render

The project is also deployed live here:  
https://bike-demand-arima.onrender.com

### How I Deployed It:

1. Pushed all project files to a GitHub repo
2. Logged into [https://render.com](https://render.com)
3. Created a new **Web Service**
4. Connected my GitHub repo

### Render Settings:

```
Build command: pip install -r requirements.txt
Start command: gunicorn app:app
```

This allowed me to host the app with no server maintenance.

---

## Project Structure

```
BikeDemand_ARIMA_Project/
├── app.py
├── forecast_output.csv
├── Bike_ARIMA_Prediction.ipynb
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/ (optional)
```

---

## Output Example

- Predicted demand for the **next hour**
- Clean, styled web interface built with Flask + HTML + GSAP
- Simple “Predict” button shows the result instantly

---

## About

This project was a great opportunity to get hands-on with time-series forecasting using the ARIMA model. I learned how to:

- Preprocess and analyze real-world time-series data
- Apply ARIMA for short-term forecasting
- Evaluate model performance using MAE and RMSE
- Build and deploy a machine learning web app using Flask

It was developed as part of my **AICTE Virtual Internship (AI Domain)**, where I combined data science, web development, and deployment to create a complete end-to-end solution.

