
# Stock-Price-Prediction-using-simple-Neural-Network             

[Data Collection](#data-collection)

[Exploratory Data Analysis](#exploratory-data-analysis)

[Data Preprocessing](#data-preprocessing)

[Model Building](#model-building)

[Model Evaluation](#model-evaluation)

[Visualization of Results](#visualization-of-results)

[Model Saving](#model-saving)



## Data Collection

- Uses the Yahoo Finance API (yfinance) to fetch 20 years of historical stock price data.
- Example ticker: GOOG (Google).
- Data includes: Open, High, Low, Close, Adj Close, and Volume.
- Purpose: Build a reliable dataset for training the pr

## Exploratory Data Analysis

- Examines dataset shape, data types, and missing values.
  
- Plots the closing price trend to visualize long-term market movement.
<img width="371" height="212" alt="image" src="https://github.com/user-attachments/assets/66c58c26-e404-4672-8b22-2e9c3c77c1e5" />

- Generates plots for all stock features (Open, High, Low, Volume, etc.).
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/784d646e-0d7a-42db-ae40-4b9cf6a131c7" />
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/6fb4a80c-8778-4f7b-abba-437ac172e52c" />
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/7df6b062-d35d-4fa6-93fb-e25660846f7f" />
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/7da41984-cf50-4b19-a23f-aad922b73334" />
<img width="452" height="159" alt="image" src="https://github.com/user-attachments/assets/f0846617-64da-4886-aa5e-a6d534253389" />

- Calculates and visualizes Moving Averages (100-day & 250-day) to capture long-term vs. short-term trends.
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/a7ec4259-be51-4d73-a62b-eeca9295696b" />
<img width="452" height="179" alt="image" src="https://github.com/user-attachments/assets/1f99d4f8-2cc6-4253-9912-20e6d23661fd" />
<img width="452" height="160" alt="image" src="https://github.com/user-attachments/assets/7315a29d-52df-4579-a4b4-05ce91ddeba7" />

- Computes percentage change in closing price to study volatility.
<img width="452" height="158" alt="image" src="https://github.com/user-attachments/assets/5643b309-9f0f-48cb-a42b-19de794d0d5d" />

- Purpose: Understand data behavior and uncover useful patterns.

## Data Preprocessing

Applies MinMaxScaler to normalize stock price data between 0 and 1.

Converts the time-series into a supervised learning problem using a sliding window:

Previous 100 days → Predict next day’s closing price.

Splits dataset into 70% training and 30% testing.

Purpose: Prepare the data so the neural network can learn efficiently.
