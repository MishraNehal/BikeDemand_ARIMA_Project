from flask import Flask, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained ARIMA model
model = joblib.load('arima_bike_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict')
def predict():
    # Forecast next 1 day
    forecast = model.forecast(steps=1)
    predicted_value = int(forecast.iloc[0])  # <- Fixed line

    return render_template(
        'index.html',
        prediction_text=f'Predicted: {predicted_value}',
        confidence_level=95,
        time_frame="Next 24h"
    )


if __name__ == '__main__':
    app.run(debug=True)
