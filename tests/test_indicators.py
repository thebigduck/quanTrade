# tests/test_indicators.py

import unittest
from src.indicators import (
    calculate_total_sell_volume,
    calculate_sell_to_buy_ratio,
    calculate_order_book_imbalance
)

class TestIndicators(unittest.TestCase):
    def setUp(self):
        self.order_book_data = {
            'bids': [{'price': 100.0, 'size': 50}, {'price': 99.5, 'size': 30}],
            'asks': [{'price': 100.5, 'size': 40}, {'price': 101.0, 'size': 20}]
        }

    def test_calculate_total_sell_volume(self):
        total_sell_volume = calculate_total_sell_volume(self.order_book_data)
        self.assertEqual(total_sell_volume, 60)

    def test_calculate_sell_to_buy_ratio(self):
        ratio = calculate_sell_to_buy_ratio(self.order_book_data)
        expected_ratio = 60 / 80  # Total asks size / Total bids size
        self.assertEqual(ratio, expected_ratio)

    def test_calculate_order_book_imbalance(self):
        imbalance = calculate_order_book_imbalance(self.order_book_data)
        expected_imbalance = (80 - 60) / (80 + 60)  # (Total bids size - Total asks size) / (Total bids size + Total asks size)
        self.assertAlmostEqual(imbalance, expected_imbalance)

if __name__ == '__main__':
    unittest.main()
