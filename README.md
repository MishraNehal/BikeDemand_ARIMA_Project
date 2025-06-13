# Bike Demand Prediction using ARIMA

## 📌 Problem
Predict daily bike rentals based on historical demand using ARIMA time-series forecasting.

## 📊 Dataset
- UCI Bike Sharing Dataset (day.csv)

## ⚙️ Model
- ARIMA (AutoRegressive Integrated Moving Average)
- Evaluated using RMSE and MAE

## 💻 Training
- Use `Bike_ARIMA_Prediction.ipynb` in Google Colab or Jupyter

## 🛠 Requirements
```bash
pip install flask joblib pandas statsmodels
```

## 🚀 Deployment (Local)
1. Run the notebook and save model using joblib
2. Place `arima_bike_model.pkl` in root
3. Run Flask app:
```bash
python app.py
```

## 🌐 Deploy to Render
1. Push all files to a GitHub repo
2. Go to [https://render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

## 🧠 Author
AICTE Internship Project | ARIMA Forecasting | Powered by ChatGPT
