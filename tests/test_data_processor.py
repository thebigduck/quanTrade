import unittest
import pandas as pd
from src.data_processor import preprocess_data

class TestDataProcessor(unittest.TestCase):
    def test_preprocess_data(self):
        data = pd.DataFrame({
            'Close': [100, 101, 102, None, 104],
            'Volume': [1000, 1100, 1200, 1300, 1400]
        })
        processed_data = preprocess_data(data)
        self.assertFalse(processed_data.isnull().values.any())
        self.assertIn('Returns', processed_data.columns)

if __name__ == '__main__':
    unittest.main()
