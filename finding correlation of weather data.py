import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clean_data.csv')


energy_cols = [col for col in df.columns if 'Energy_Meter' in col]
df['Total_Consumption'] = df[energy_cols].sum(axis=1)


weather_vars = ['Avg_Temp', 'Avg_Rel_Humidity', 'Avg_Wind_Speed', 'Total_Global_Rad']

# 4. Calculate Correlation
corr_values = df[weather_vars + ['Total_Consumption']].corr()['Total_Consumption'].drop('Total_Consumption')


plt.figure(figsize=(12, 6))
corr_values.plot(kind='bar', color=['#4c72b0', '#55a868', '#c44e52', '#8172b2'])
plt.title('Correlation of Weather Variables with Total Energy Consumption')
plt.ylabel('Correlation Coefficient (r)')
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()
