import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('mean_days_data.csv')

# Convert time column
df['Time'] = pd.to_datetime(df['Time'])

#  Use already available total consumption
data = df[['Time', 'Total_Consumption']].copy()

#  IMPORTANT: Convert 15-min data → DAILY TOTAL
daily_data = data.resample('D', on='Time').sum().reset_index()

# Rename for Prophet
daily_data.rename(columns={'Time': 'ds', 'Total_Consumption': 'y'}, inplace=True)

# Train model
model = Prophet()
model.fit(daily_data)

# Create future (6 months ≈ 180 days)
future = model.make_future_dataframe(periods=180, freq='D')

# Predict
forecast = model.predict(future)

# Take only future predictions
future_forecast = forecast[['ds', 'yhat']].tail(180)

#Convert to MONTHLY TOTAL
future_forecast['Month'] = future_forecast['ds'].dt.to_period('M')

monthly_forecast = future_forecast.groupby('Month')['yhat'].sum().reset_index()

# Rename columns
monthly_forecast.columns = ['Month', 'Total_Monthly_Consumption']
monthly_forecast['Month'] = monthly_forecast['Month'].astype(str)

#  PRINT RESULT
print("\nTotal Monthly Energy Consumption Forecast:\n")
print(monthly_forecast.to_string(index=False))

#  BAR CHART
plt.figure(figsize=(10,5))
plt.bar(monthly_forecast['Month'], monthly_forecast['Total_Monthly_Consumption'])

plt.title("6-Month Energy Consumption Forecast (All 172 Meters)")
plt.xlabel("Month")
plt.ylabel("Total Consumption")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()