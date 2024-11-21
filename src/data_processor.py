def preprocess_data(data):
    """
    Cleans and preprocesses the raw stock data.
    """
    data = data.dropna()
    data['returns'] = data['close'].pct_change()  # Use 'close' in lowercase
    return data