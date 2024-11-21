# src/data_processor.py

def preprocess_data(data):
    """
    Cleans and preprocesses the raw stock data.
    """
    data = data.dropna()
    data['returns'] = data['adj close'].pct_change()  # Use 'adj close' for returns
    return data
