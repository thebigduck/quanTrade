# src/data_fetcher.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    # Ensure ticker is a string
    ticker = str(ticker).strip().upper()
    print(f"Ticker: {ticker}, Type: {type(ticker)}")

    # Fetch data using yfinance
    data = yf.download(ticker, start=start_date, end=end_date, group_by='column')

    # Verify Column Names
    print("Original Columns:", data.columns)

    # If columns are MultiIndex, flatten them
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
        print("Flattened Columns:", data.columns)
        
# Convert column names to lowercase
    data.columns = [col.lower() for col in data.columns]
    print("Columns Lowercase:", data.columns)  # Add this line

    # Drop any rows with missing data
    data.dropna(inplace=True)
    return data
