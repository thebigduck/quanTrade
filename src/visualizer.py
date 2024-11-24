# src/visualizer.py

"""
Module for creating visualizations for the application.
"""

import matplotlib.pyplot as plt

def plot_order_book_depth(order_book_data):
    """
    Plots the order book depth chart.

    Parameters:
        order_book_data (dict): Order book data containing 'bids' and 'asks'.

    Returns:
        matplotlib.figure.Figure: The figure object containing the plot.
    """
    bids = order_book_data["bids"]
    asks = order_book_data["asks"]

    bid_prices = [bid["price"] for bid in bids]
    bid_sizes = [bid["size"] for bid in bids]

    ask_prices = [ask["price"] for ask in asks]
    ask_sizes = [ask["size"] for ask in asks]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot bids
    ax.bar(bid_prices, bid_sizes, color="green", width=0.01, align="edge", label="Bids")

    # Plot asks
    ax.bar(ask_prices, ask_sizes, color="red", width=-0.01, align="edge", label="Asks")

    ax.set_xlabel("Price")
    ax.set_ylabel("Size")
    ax.set_title("Order Book Depth")
    ax.legend()

    return fig

def plot_backtest_results(equity_curve):
    """
    Plots the equity curve from the backtest.

    Parameters:
        equity_curve (pandas.Series): The equity curve over time.

    Returns:
        matplotlib.figure.Figure: The figure object containing the plot.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    equity_curve.plot(ax=ax)
    ax.set_title("Equity Curve")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")
    return fig
