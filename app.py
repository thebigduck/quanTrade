import streamlit as st
import pandas as pd

from src.data_fetcher import fetch_stock_data
from src.data_processor import preprocess_data
from src.backtester import run_backtest
from src.strategies.sma_crossover import SmaCrossoverStrategy
from src.config import DEFAULT_TICKER, START_DATE, END_DATE

st.title('Quantitative Trading App')

# Input fields
ticker_input = st.text_input('Enter Stock Ticker', DEFAULT_TICKER)
start_date = st.date_input('Start Date', pd.to_datetime(START_DATE))
end_date = st.date_input('End Date', pd.to_datetime(END_DATE))

# Validate and sanitize ticker input
ticker = str(ticker_input).strip().upper()
if ',' in ticker or ' ' in ticker:
    st.error('Please enter a single ticker symbol without spaces or commas.')
    st.stop()

# Run backtest button
if st.button('Run Backtest'):
    data = fetch_stock_data(ticker, start_date, end_date)
    if not data.empty:
        processed_data = preprocess_data(data)
        fig = run_backtest(processed_data, SmaCrossoverStrategy)
        # Display the plot in Streamlit
        st.pyplot(fig)
    else:
        st.error('No data available for backtesting.')
