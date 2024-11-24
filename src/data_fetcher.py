# src/data_fetcher.py

import alpaca_trade_api as tradeapi
from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL
import logging

# Initialize logging
logger = logging.getLogger(__name__)

# Initialize the Alpaca API client
api = tradeapi.REST(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    base_url=ALPACA_BASE_URL
)

def fetch_order_book_data(ticker):
    """
    Fetches Level II order book data for the specified ticker.

    Parameters:
        ticker (str): The stock ticker symbol.

    Returns:
        dict: Order book data containing bids and asks.
    """
    try:
        order_book = api.get_orderbook(ticker)
        return {
            'bids': [{'price': float(b.price), 'size': float(b.size)} for b in order_book.bids],
            'asks': [{'price': float(a.price), 'size': float(a.size)} for a in order_book.asks]
        }
    except Exception as e:
        logger.error(f"Error fetching order book data for {ticker}: {e}")
        return None

def fetch_historical_data(ticker, start_date, end_date):
    """
    Fetches historical price data for the specified ticker and date range.

    Parameters:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: Historical price data.
    """
    try:
        barset = api.get_bars(
            symbol=ticker,
            timeframe='1Day',
            start=start_date,
            end=end_date,
            adjustment='raw'
        ).df
        return barset
    except Exception as e:
        logger.error(f"Error fetching historical data for {ticker}: {e}")
        return None
