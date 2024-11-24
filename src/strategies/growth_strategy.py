# src/strategies/growth_strategy.py

"""
Trading strategy that uses the stock growth predictions from the machine learning model.
"""

import backtrader as bt
from src.models.stock_growth_predictor import predict_growth_potential
from src.data_fetcher import fetch_order_book_data

class GrowthStrategy(bt.Strategy):
    params = dict(
        model_refresh_period=1,  # Number of days between model updates
    )

    def __init__(self):
        self.order = None
        self.counter = 0

    def next(self):
        # Skip days if not time to refresh model
        if self.counter % self.p.model_refresh_period != 0:
            self.counter += 1
            return

        # Get current ticker symbol
        ticker = self.datas[0]._name

        # Fetch order book data
        order_book_data = fetch_order_book_data(ticker)
        if order_book_data is None:
            return

        # Get prediction
        prediction, probability = predict_growth_potential(order_book_data)

        # Trading logic
        if not self.position:
            if prediction == 1:
                # Buy signal
                self.order = self.buy()
        else:
            if prediction == 0:
                # Sell signal
                self.order = self.sell()

        self.counter += 1

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                print(f"Bought at {order.executed.price}")
            elif order.issell():
                print(f"Sold at {order.executed.price}")
        self.order = None
