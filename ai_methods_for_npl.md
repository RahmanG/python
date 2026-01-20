# AI/ML Approach: Predicting NPLs with Macroeconomic Indicators

This document outlines how to apply Artificial Intelligence and Machine Learning models to the research topic: **"Impact of Macroeconomic Variables on Non-Performing Loans (NPLs) in Bangladesh."**

## 1. Why Use AI over Traditional Econometrics?
- **Non-Linearity:** Traditional models (OLS, VECM) assume linear relationships. AI models (Neural Networks, Random Forests) can capture complex, non-linear interactions between inflation, GDP, and NPLs.
- **Predictive Power:** ML models often outperform statistical models in pure forecasting accuracy (RMSE/MAE).
- **Feature Importance:** Advanced tree-based models provide detailed insights into *which* variable matters most.

## 2. Methodology Adjustment

### A. Data Pre-processing (Crucial for AI)
AI models don't understand "time" natively like ARIMA. You must transform the data:
1.  **Sliding Window / Lag Features:** Create input features based on past values.
    - *Input (X):* [GDP(t-1), Inflation(t-1), NPL(t-1), GDP(t-2)...]
    - *Target (Y):* NPL(t)
2.  **Normalization/Scaling:** Neural Networks (LSTM) require data to be scaled (e.g., MinMax Scaler to 0-1 range).
3.  **Stationarity:** While less critical for Trees, transforming non-stationary data (using differencing) helps LSTMs converge faster.

### B. Suggested Models

#### 1. Long Short-Term Memory (LSTM) / GRU
- **Type:** Deep Learning (Recurrent Neural Network).
- **Why:** specifically designed for sequence data. It "remembers" long-term dependencies (e.g., an economic shock 2 years ago affecting NPLs today).
- **Implementation:** Python (`Keras` / `TensorFlow` / `PyTorch`).

#### 2. XGBoost / LightGBM / Random Forest
- **Type:** Gradient Boosting / Ensemble Methods.
- **Why:** Excellent at handling tabular data and capturing non-linear thresholds (e.g., "If Inflation > 6%, NPL spikes drastically").
- **Implementation:** Python (`xgboost`, `sklearn`).

#### 3. Support Vector Regression (SVR)
- **Type:** Kernel-based classical ML.
- **Why:** Works well with smaller datasets (which macro data often is—e.g., only 50-100 data points).

## 3. Explainable AI (XAI)
One criticism of AI is the "Black Box" nature. You can solve this using:
- **SHAP (SHapley Additive exPlanations):**
  - It tells you exactly how much each feature contributed to a prediction.
  - *Example Finding:* "High Inflation increased the predicted NPL by 2%, but high GDP Growth reduced it by 1.5%."

## 4. Proposed Experiment Structure

1.  **Baseline:** Run a simple Linear Regression or ARIMA model.
2.  **AI Model:** Train an LSTM or XGBoost model on the same data.
3.  **Comparison:** Compare metrics:
    - **RMSE (Root Mean Square Error):** Lower is better.
    - **MAPE (Mean Absolute Percentage Error):** Easier to interpret (e.g., "The model is off by 5% on average").

## 5. Sample Python Workflow

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1. Load Data
df = pd.read_csv('bangladesh_macro_npl.csv')

# 2. Preprocess (Scale & Window)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['NPL', 'Inflation', 'GDP', 'LendingRate']])
# ... function to convert to X, y sequences ...

# 3. Build LSTM Model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# 4. Train
model.fit(X_train, y_train, epochs=200, verbose=0)
```

## 6. Challenges to Address in Thesis
- **Small Sample Size:** Macro data is usually annual or quarterly. If you have data from 2000-2023, that's only ~92 quarterly points. Deep Learning (LSTM) might overfit.
  - *Solution:* Use "Bootstrapping" or simpler ML models (Random Forest/SVR) if data is scarce. Focus on quarterly data to maximize N.
