import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

st.title("Stock Price Predictor App")

stock = st.text_input("Enter the Stock ID", "GOOG")

# Fetch Stock Data
end = datetime.now()
start = datetime(end.year - 20, end.month, end.day)

google_data = yf.download(stock, start, end)

if google_data.empty:
    st.error("No data found for the entered stock ID. Please try again.")
    st.stop()

# Load Pre-trained Model
model = load_model("Latest_stock_price_model.keras")

st.subheader("Stock Data")
st.write(google_data)

# Ensure 'Close' Column Exists
if 'Close' not in google_data.columns:
    st.error("No 'Close' price data available in the dataset.")
    st.stop()

# Prepare Test Data
splitting_len = int(len(google_data) * 0.7)
x_test = pd.DataFrame(google_data['Close'][splitting_len:])

# Moving Averages
google_data['MA_for_250_days'] = google_data['Close'].rolling(250).mean()
google_data['MA_for_200_days'] = google_data['Close'].rolling(200).mean()
google_data['MA_for_100_days'] = google_data['Close'].rolling(100).mean()

def plot_graph(figsize, values, full_data, extra_data=0, extra_dataset=None):
    fig = plt.figure(figsize=figsize)
    plt.plot(values, 'Orange')
    plt.plot(full_data['Close'], 'b')
    if extra_data:
        plt.plot(extra_dataset)
    return fig

st.subheader('Original Close Price and MA for 250 days')
st.pyplot(plot_graph((15,6), google_data['MA_for_250_days'], google_data))

st.subheader('Original Close Price and MA for 200 days')
st.pyplot(plot_graph((15,6), google_data['MA_for_200_days'], google_data))

st.subheader('Original Close Price and MA for 100 days')
st.pyplot(plot_graph((15,6), google_data['MA_for_100_days'], google_data))

st.subheader('Original Close Price and MA for 100 days and MA for 250 days')
st.pyplot(plot_graph((15,6), google_data['MA_for_100_days'], google_data, 1, google_data['MA_for_250_days']))

# Scaling Data
scaler = MinMaxScaler(feature_range=(0,1))

if not x_test.empty:
    scaled_data = scaler.fit_transform(x_test)
else:
    st.error("No test data available after split.")
    st.stop()

# Prepare Input Data for Prediction
x_data, y_data = [], []
for i in range(100, len(scaled_data)):
    x_data.append(scaled_data[i-100:i])
    y_data.append(scaled_data[i])

x_data, y_data = np.array(x_data), np.array(y_data)

if x_data.shape[0] == 0:
    st.error("Not enough data points for making predictions. Try a different stock.")
    st.stop()

# Make Predictions
predictions = model.predict(x_data)
inv_pre = scaler.inverse_transform(predictions)
inv_y_test = scaler.inverse_transform(y_data)

ploting_data = pd.DataFrame({
    'original_test_data': inv_y_test.reshape(-1),
    'predictions': inv_pre.reshape(-1)
}, index=google_data.index[splitting_len+100:])

st.subheader("Original values vs Predicted values")
st.write(ploting_data)

st.subheader('Original Close Price vs Predicted Close price')
fig = plt.figure(figsize=(15,6))
plt.plot(pd.concat([google_data['Close'][:splitting_len+100], ploting_data], axis=0))
plt.legend(["Data- not used", "Original Test data", "Predicted Test data"])
st.pyplot(fig)

# python -m streamlit run "/Users/kushaldutia/Documents/Stock Price Predictor/web_stock_price_predictor.py"