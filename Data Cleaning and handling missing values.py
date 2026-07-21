import pandas as pd
#for energy data, we have some missing values, so we will use interpolation to fill those missing values. We will use time-based interpolation since our data is time-series data. After interpolation, we will also use forward fill and backward fill to ensure that there are no remaining missing values in the dataset.
energy = pd.read_csv('loureiro_energy.csv')
energy['Time'] = pd.to_datetime(energy['Time'], format='%d-%m-%Y %H:%M')
energy= energy.set_index('Time').interpolate(method='time')
energy= energy.interpolate().ffill().bfill()
#for weater data, we have some missing values, so we will use interpolation to fill those missing values. We will use time-based interpolation since our data is time-series data. After interpolation, we will also use forward fill and backward fill to ensure that there are no remaining missing values in the dataset.
weather = pd.read_csv('weather_aveiro_final.csv')
weather['Time'] = pd.to_datetime(weather['Time'], format='%d-%m-%Y %H:%M')
weather = weather.sort_values('Time')
weather= weather.set_index('Time').interpolate(method='time')   
weather= weather.interpolate().ffill().bfill()
#Data merging: We will merge the energy and weather datasets on the 'Time' column. This will allow us to have a single dataset that contains both energy consumption and weather data for each time point.
data = pd.merge(energy, weather, on='Time')
data.to_csv('merged_data.csv')
#Data cleaning: We will check for any remaining missing values in the merged dataset and handle them appropriately. We will also check for any outliers in the data and handle them as well. Finally, we will save the cleaned dataset to a new CSV file for further analysis.
import numpy as np
data = data.replace(0, np.nan)
null_percentage = data.isnull().sum() / len(data) * 100
cols_to_drop = null_percentage[null_percentage > 99].index
data = data.drop(columns=cols_to_drop)
print("Dropped columns:", list(cols_to_drop))
#After dropping columns with more than 99% missing values, we will drop columns of weather data that are not relevant for our analysis.
data = data.drop(columns=['Max_Inst_Wind_Speed','Inst_Temp','Avg_Wind_Direction','Avg_Wind_Direction'])
print(data.columns)
data = data.replace(np.nan, 0)
data.to_csv('cleaned_data.csv')


print("Print New Update on line")










