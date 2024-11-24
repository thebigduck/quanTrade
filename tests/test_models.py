# tests/test_models.py

import unittest
import pandas as pd
from src.models.model_training import prepare_training_data, train_growth_model
from src.models.stock_growth_predictor import predict_growth_potential
from src.data_fetcher import fetch_order_book_data
import os

class TestModels(unittest.TestCase):
    def test_model_training(self):
        # Prepare mock data
        order_books = {
            '2022-01-01': {
                'bids': [{'price': 100.0, 'size': 50}],
                'asks': [{'price': 100.5, 'size': 40}]
            }
            # Add more snapshots
        }
        price_data = pd.DataFrame({
            'close': [100, 102],
            'date': ['2022-01-01', '2022-01-02']
        }).set_index('date')

        X, y = prepare_training_data(order_books, price_data)
        self.assertFalse(X.empty)
        self.assertFalse(y.empty)

        # Train model
        train_growth_model(X, y)
        model_path = os.path.join('data/models/', 'growth_model.pkl')
        self.assertTrue(os.path.exists(model_path))

    def test_predict_growth_potential(self):
        # Fetch sample order book data
        ticker = 'AAPL'
        order_book_data = fetch_order_book_data(ticker)
        if order_book_data:
            prediction, probability = predict_growth_potential(order_book_data)
            self.assertIn(prediction, [0, 1])
            self.assertTrue(0 <= probability <= 1)
        else:
            self.skipTest('Order book data not available')

if __name__ == '__main__':
    unittest.main()
