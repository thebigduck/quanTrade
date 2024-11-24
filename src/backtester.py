# src/backtester.py

"""
Module for backtesting trading strategies using historical data.
"""

import backtrader as bt
from datetime import datetime
import pandas as pd
from src.data_fetcher import fetch_historical_data
from src.strategies.growth_strategy import GrowthStrategy
from src.config import DATA_DIR
import os

def run_backtest(ticker, start_date="2020-01-01", end_date=None):
    """
    Runs a backtest on the specified ticker using the GrowthStrategy.

    Parameters:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date for the backtest in 'YYYY-MM-DD' format.
        end_date (str): The end date for the backtest in 'YYYY-MM-DD' format. Defaults to today.

    Returns:
        dict: Backtest performance metrics and equity curve.
    """
    try:
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")

        # Fetch historical data
        data = fetch_historical_data(ticker, start_date, end_date)
        if data is None or data.empty:
            print("No historical data available.")
            return None

        data.index = pd.to_datetime(data.index)
        data_feed = bt.feeds.PandasData(dataname=data)

        # Initialize Cerebro engine
        cerebro = bt.Cerebro()
        cerebro.addstrategy(GrowthStrategy)
        cerebro.adddata(data_feed)
        cerebro.broker.setcash(100000.0)  # Starting cash
        cerebro.broker.setcommission(commission=0.001)  # Commission of 0.1%

        # Run backtest
        print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
        cerebro.run()
        final_value = cerebro.broker.getvalue()
        print("Final Portfolio Value: %.2f" % final_value)

        # Calculate performance metrics
        total_return = (final_value - 100000.0) / 100000.0
        sharpe_ratio = calculate_sharpe_ratio(cerebro)
        max_drawdown = calculate_max_drawdown(cerebro)

        # Get equity curve
        equity_curve = get_equity_curve(cerebro)

        results = {
            "total_return": total_return,
            "sharpe_ratio": sharpe_ratio,
            "max_drawdown": max_drawdown,
            "equity_curve": equity_curve,
        }

        return results

    except Exception as e:
        print(f"Error running backtest: {e}")
        return None

def calculate_sharpe_ratio(cerebro):
    """
    Calculates the Sharpe Ratio of the strategy.

    Parameters:
        cerebro (bt.Cerebro): The backtesting engine instance.

    Returns:
        float: The Sharpe Ratio.
    """
    # Placeholder for actual implementation
    # You can use cerebro.analyzers to get performance metrics
    return 1.5  # Example value

def calculate_max_drawdown(cerebro):
    """
    Calculates the Maximum Drawdown of the strategy.

    Parameters:
        cerebro (bt.Cerebro): The backtesting engine instance.

    Returns:
        float: The maximum drawdown percentage.
    """
    # Placeholder for actual implementation
    return 0.2  # Example value

def get_equity_curve(cerebro):
    """
    Retrieves the equity curve from the backtest.

    Parameters:
        cerebro (bt.Cerebro): The backtesting engine instance.

    Returns:
        pandas.DataFrame: The equity curve.
    """
    # Placeholder for actual implementation
    # You can extract the equity curve from the broker or analyzers
    dates = pd.date_range(start="2020-01-01", periods=100)
    equity = pd.Series(100000 + (dates.dayofyear * 10), index=dates)
    return equity
