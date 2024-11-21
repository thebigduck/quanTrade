# src/visualizer.py

import matplotlib.pyplot as plt
import streamlit as st 

def plot_stock_data(data, ticker):
    """
    Plots the closing price of the stock.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['close'], label='Close Price')  # Use 'close' in lowercase
    plt.title(f'{ticker} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)  # Use st.pyplot() to display in Streamlit
