from flask import Flask, render_template, send_file
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    # Step 1: Load the last 200 hours of data
    df = pd.read_csv('hour.csv')
    ts = df['cnt'].tail(200)

    # Step 2: Train ARIMA model
    model = ARIMA(ts, order=(3, 1, 2))
    model_fit = model.fit()

    # Step 3: Forecast next hour
    forecast = model_fit.forecast(steps=1)
    predicted_value = int(forecast.iloc[0])

    # Step 4: Save to CSV with timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_df = pd.DataFrame({
        "timestamp": [now],
        "predicted_count": [predicted_value]
    })
    output_df.to_csv("forecast_output.csv", index=False)

    return render_template(
        'index.html',
        prediction_text=f'Predicted: {predicted_value}',
        confidence_level=95,
        time_frame="Next Hour"
    )

# Step 5: Route to download the file
@app.route('/download')
def download_csv():
    return send_file("forecast_output.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
