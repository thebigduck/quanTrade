# src/models/stock_growth_predictor.py

import joblib
import os
from src.config import MODEL_DIR
from src.indicators import (
    calculate_total_sell_volume,
    calculate_sell_to_buy_ratio,
    calculate_order_book_imbalance
)

# Load the trained model
model_path = os.path.join(MODEL_DIR, 'growth_model.pkl')
model = joblib.load(model_path)

def predict_growth_potential(order_book_data):
    """
    Predicts the stock growth potential based on order book data.

    Parameters:
        order_book_data (dict): Order book data containing 'bids' and 'asks'.

    Returns:
        tuple: Prediction (0 or 1), Probability of positive class.
    """
    # Calculate indicators
    total_sell_volume = calculate_total_sell_volume(order_book_data)
    sell_to_buy_ratio = calculate_sell_to_buy_ratio(order_book_data)
    order_book_imbalance = calculate_order_book_imbalance(order_book_data)

    # Create feature vector
    features = [[
        total_sell_volume,
        sell_to_buy_ratio,
        order_book_imbalance
    ]]

    # Make prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # Probability of class 1
    return prediction, probability
