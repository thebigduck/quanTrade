import unittest
import pandas as pd
from src.backtester import run_backtest
from src.strategies.sma_crossover import SmaCrossoverStrategy

class TestBacktester(unittest.TestCase):
    def test_run_backtest(self):
        data = pd.DataFrame({
            'Open': [100, 101, 102, 103, 104],
            'High': [101, 102, 103, 104, 105],
            'Low': [99, 100, 101, 102, 103],
            'Close': [100, 101, 102, 103, 104],
            'Volume': [1000, 1100, 1200, 1300, 1400],
            'Adj Close': [100, 101, 102, 103, 104]
        }, index=pd.date_range('2020-01-01', periods=5))
        try:
            run_backtest(data, SmaCrossoverStrategy)
        except Exception as e:
            self.fail(f"Backtest failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
