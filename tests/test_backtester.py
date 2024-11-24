# tests/test_backtester.py

"""
Unit tests for the backtesting module.
"""

import unittest
from src.backtester import run_backtest

class TestBacktester(unittest.TestCase):
    def test_run_backtest(self):
        ticker = "AAPL"
        results = run_backtest(ticker, start_date="2020-01-01", end_date="2020-12-31")
        self.assertIsNotNone(results)
        self.assertIn("total_return", results)
        self.assertIn("sharpe_ratio", results)
        self.assertIn("max_drawdown", results)
        self.assertIn("equity_curve", results)

if __name__ == "__main__":
        unittest.main()
