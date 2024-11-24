# src/models/model_training.py

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.config import MODEL_DIR
from src.indicators import (
    calculate_total_sell_volume,
    calculate_sell_to_buy_ratio,
    calculate_order_book_imbalance
)

def prepare_training_data(order_books, price_data):
    """
    Prepares training data by calculating indicators and labeling based on future price movements.

    Parameters:
        order_books (list): List of order book snapshots.
        price_data (pandas.DataFrame): Historical price data.

    Returns:
        pandas.DataFrame: Features DataFrame.
        pandas.Series: Target variable.
    """
    features = []
    targets = []

    for timestamp, order_book in order_books.items():
        # Calculate indicators
        total_sell_volume = calculate_total_sell_volume(order_book)
        sell_to_buy_ratio = calculate_sell_to_buy_ratio(order_book)
        order_book_imbalance = calculate_order_book_imbalance(order_book)

        # Feature vector
        feature_vector = {
            'total_sell_volume': total_sell_volume,
            'sell_to_buy_ratio': sell_to_buy_ratio,
            'order_book_imbalance': order_book_imbalance
        }

        # Get future price movement (e.g., next day's return)
        current_price = price_data.loc[timestamp]['close']
        future_timestamp = price_data.index[price_data.index.get_loc(timestamp) + 1] if price_data.index.get_loc(timestamp) + 1 < len(price_data) else None

        if future_timestamp:
            future_price = price_data.loc[future_timestamp]['close']
            price_return = (future_price - current_price) / current_price
            target = 1 if price_return > 0.02 else 0  # 2% growth threshold
            features.append(feature_vector)
            targets.append(target)

    X = pd.DataFrame(features)
    y = pd.Series(targets)
    return X, y

def train_growth_model(X, y):
    """
    Trains a Random Forest classifier and saves the model.

    Parameters:
        X (pandas.DataFrame): Features.
        y (pandas.Series): Target variable.
    """
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)

    # Save the model
    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, 'growth_model.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
