# tests/test_data_fetcher.py

import unittest
from src.data_fetcher import fetch_order_book_data, fetch_historical_data

class TestDataFetcher(unittest.TestCase):
    def test_fetch_order_book_data(self):
        ticker = 'AAPL'
        data = fetch_order_book_data(ticker)
        self.assertIsNotNone(data)
        self.assertIn('bids', data)
        self.assertIn('asks', data)

    def test_fetch_historical_data(self):
        ticker = 'AAPL'
        data = fetch_historical_data(ticker, '2022-01-01', '2022-01-10')
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
