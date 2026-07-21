import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("clean_data.csv")
df["Time"] = pd.to_datetime(df["Time"], format="%d-%m-%Y %H:%M")
df.set_index("Time", inplace=True)

# Select energy meter columns
energy_cols = [col for col in df.columns if "Energy_Meter" in col]


# Calculate total consumption for the raw (e.g., 15-min) data
df['Total_Consumption'] = df[energy_cols].sum(axis=1)

# Extract hour and day of week for pattern analysis
df['Hour'] = df.index.hour
df['DayOfWeek'] = df.index.day_name()

# Analyze hourly and daily patterns in energy consumption
hourly_pattern = df.groupby('Hour')['Total_Consumption'].mean()
daily_pattern = df.groupby('DayOfWeek')['Total_Consumption'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Identify top 3 peak hours
top_peaks = hourly_pattern.sort_values(ascending=False).head(3)
print("Top 3 Peak Hours:\n", top_peaks)

# --- Plot 1: Daily Usage Pattern (Average Hourly Consumption) ---
plt.figure(figsize=(15, 7))
sns.lineplot(data=hourly_pattern, marker='o', color='teal')
for i, v in enumerate(hourly_pattern.values):
    plt.text(i, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

plt.xticks(range(0, 24))
plt.title('Daily Usage Pattern (Average Hourly Consumption)')
plt.xlabel('Hour of Day (24h)')
plt.ylabel('Total Energy Units')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# --- Plot 2: Monthly Energy Usage Patterns ---
monthly_data = df.groupby(df.index.to_period('M'))['Total_Consumption'].mean()
monthly_data.index = monthly_data.index.astype(str)

plt.figure(figsize=(14, 7))
sns.barplot(x=monthly_data.index, y=monthly_data.values, palette='magma')

for i, v in enumerate(monthly_data.values):
    plt.text(i, v + (0.02 * v), f'{v:.2f}', ha='center', fontweight='bold')

plt.title('Monthly Energy Usage Patterns')
plt.xlabel('Month (YYYY-MM)')
plt.ylabel('Average Units Consumed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Weekday vs Weekend Comparison
# Convert granular data to hourly sums
hourly_data = df[energy_cols].resample("h").sum()

hourly_data["Total"] = hourly_data.sum(axis=1)

hourly_data["DayType"] = hourly_data.index.dayofweek.map(
    lambda x: "Weekend" if x >= 5 else "Weekday"
)
hourly_data["Hour"] = hourly_data.index.hour

weekday_avg = hourly_data[hourly_data["DayType"] == "Weekday"].groupby("Hour")["Total"].mean()
weekend_avg = hourly_data[hourly_data["DayType"] == "Weekend"].groupby("Hour")["Total"].mean()

# --- Plot 3: Weekday vs Weekend Hourly Energy Consumption ---
plt.figure(figsize=(12, 6))
plt.plot(weekday_avg.index, weekday_avg.values, label="Weekday", marker='o')
plt.plot(weekend_avg.index, weekend_avg.values, label="Weekend", marker='s')

plt.xlabel("Hour of Day")
plt.ylabel("Average Consumption (kWh)")
plt.title("Weekday vs Weekend Hourly Energy Consumption")
plt.xticks(range(0, 24))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()