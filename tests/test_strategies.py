# tests/test_strategies.py

"""
Unit tests for trading strategies.
"""

import unittest
from src.strategies.growth_strategy import GrowthStrategy
import backtrader as bt
from src.data_fetcher import fetch_historical_data

class TestStrategies(unittest.TestCase):
    def test_growth_strategy(self):
        ticker = "AAPL"
        data = fetch_historical_data(ticker, "2020-01-01", "2020-12-31")
        data.index = pd.to_datetime(data.index)
        data_feed = bt.feeds.PandasData(dataname=data)

        cerebro = bt.Cerebro()
        cerebro.addstrategy(GrowthStrategy)
        cerebro.adddata(data_feed)
        cerebro.broker.setcash(100000.0)

        cerebro.run()
        final_value = cerebro.broker.getvalue()
        self.assertGreater(final_value, 0)

if __name__ == "__main__":
    unittest.main()
