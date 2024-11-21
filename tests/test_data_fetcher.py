import unittest
from src.data_fetcher import fetch_stock_data

class TestDataFetcher(unittest.TestCase):
    def test_fetch_stock_data(self):
        data = fetch_stock_data('AAPL', '2020-01-01', '2020-01-10')
        self.assertFalse(data.empty)
        self.assertIn('Close', data.columns)

if __name__ == '__main__':
    unittest.main()
