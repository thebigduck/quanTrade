import unittest
import pandas as pd
import backtrader as bt
from src.strategies.sma_crossover import SmaCrossoverStrategy

class TestStrategies(unittest.TestCase):
    def test_sma_crossover_strategy(self):
        data = pd.DataFrame({
            'Open': [100, 102, 104, 103, 105],
            'High': [101, 103, 105, 104, 106],
            'Low': [99, 101, 103, 102, 104],
            'Close': [100, 102, 104, 103, 105],
            'Volume': [1000, 1100, 1200, 1300, 1400],
            'Adj Close': [100, 102, 104, 103, 105]
        }, index=pd.date_range('2020-01-01', periods=5))
        cerebro = bt.Cerebro()
        cerebro.addstrategy(SmaCrossoverStrategy)
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        cerebro.run()
        # Test passes if no exceptions are raised

if __name__ == '__main__':
    unittest.main()
