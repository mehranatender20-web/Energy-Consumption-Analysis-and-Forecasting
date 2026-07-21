# Smart Energy Consumption and Forecasting

A capstone project analyzing 15-minute interval smart meter data from **172 households** in a local energy cooperative in Loureiro, Portugal, over a ~16-month period. The project cleans and merges energy + weather data, performs exploratory analysis, and builds a machine learning model to forecast electricity consumption — with actionable recommendations for households, grid operators, and energy providers.

**Student:** Natender
**Supervisor:** Professor Humera Noor Minhas
**Program:** MSc. Data Science

---

## 📌 Project Overview

Smart meters generate huge volumes of high-resolution data, but this data is rarely used to its full potential. This project analyzes household electricity usage patterns to:

- Identify peak and off-peak demand periods
- Recommend optimal times for appliance usage to reduce costs
- Help grid operators manage load distribution
- Forecast future electricity demand using machine learning
- Present findings through visual dashboards and reports

**Dataset:** [Electricity consumption dataset of a local energy cooperative](https://data.mendeley.com/datasets/vryvyfz2tj/1) — Monteiro et al., 2024 (DOI: 10.17632/vryvyfz2tj.1)

---

## 🗂️ Repository Structure

```
smart-energy-forecasting/
├── src/                          # Code files (scripts/notebooks)
│   ├── dataprocessing.py         # Data cleaning, merging, feature engineering
│   └── model.py                  # Random Forest forecasting model
├── docs/                         # PDF reports & proposal
│   ├── EDA Report
│   ├── Final Report 
├── data/                         # Raw / cleaned datasets (not tracked if large — see .gitignore)
├── dashboard/                    # Power BI / Streamlit dashboard files
└── README.md
```

> 💡 Tip: Keep `src/` for code and `docs/` for PDFs — GitHub preserves this separation automatically once files are uploaded into their respective folders

---

## 🔧 Methodology

1. **Data Collection & Understanding** – Explore energy + weather datasets, structure, and time range
2. **Data Preprocessing** – Handle missing values (interpolation, ffill/bfill), merge energy and weather data on the `Time` column, drop redundant/low-value columns
3. **Exploratory Data Analysis (EDA)** – Daily/weekly/seasonal usage patterns, weekday vs. weekend comparison, weather correlations
4. **Model Development** – Time-series forecasting using feature engineering (lag features, day-of-week, weather regressors)
5. **Insights & Recommendations** – Load-shifting proposals, dashboard visualization, forecasting insights

---

## 🔑 Key Findings

- **Double-peak daily pattern:** morning peak (~10:00–12:00) and evening peak (~20:00, highest usage)
- **Baseload period:** 03:00–05:00, lowest consumption
- **Seasonal trends:** Winter peak (January) and secondary summer peak (July); lowest usage in shoulder seasons (April, September)
- **Weekday vs weekend:** Weekends show earlier daytime usage; weekdays have sharper evening peaks
- **Weather correlation:** Humidity shows the strongest (negative) correlation with consumption; temperature/radiation show weak correlation

---

## 🤖 Forecasting Models

- **Random Forest Regressor** (Sprint 4): 100 trees, max depth 12, using lag features (15-min, 1-hr, 24-hr), day-of-week, and weather variables
  - **R² ≈ 0.939 (93.9% accuracy)**
  - MAE: 0.5404 units | RMSE: 0.7793 units
- **Facebook Prophet** (Sprints 3 & 5): Used for 6-month consumption forecasting, capturing daily/weekly/yearly seasonality

---

## 🛠️ Tools & Technologies

| Category | Tools |
|----------|-------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost, Statsmodels, Prophet, TensorFlow |
| Visualization | Matplotlib, Power BI, Streamlit |
| Environment | VS Code |

---

## 💡 Recommendations

- **Load shifting:** Split households between 1–3 AM and 3–6 AM for heavy appliance use (e.g., EV charging) to reduce peak load and take advantage of off-peak tariffs
- **Grid operators:** Use demand forecasts for better load balancing and blackout prevention
- **Energy providers:** Use forecasts for planning, pricing strategy, and demand-side management programs

---

## 🚀 Future Improvements

- Real-time weather API integration for live forecasting
- Expansion to commercial/industrial sectors
- Smart home / IoT automation integration for appliance scheduling
- Hyperparameter tuning and testing advanced models (Gradient Boosting, XGBoost, LSTM)

---

## 📚 References

- Monteiro, F., Oliveira, R., Almeida, J., Gonçalves, P., Bartolomeu, P., Neto, J., & Deus, R. (2024). *Electricity consumption dataset of a local energy cooperative.* DOI: 10.17632/vryvyfz2tj.1
- Research on smart meters, demand-side management, and time-series forecasting (ARIMA, SARIMA, LSTM)
