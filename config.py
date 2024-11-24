# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Alpaca API Credentials
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading URL

# Other configurations
DATA_DIR = 'data/'
MODEL_DIR = os.path.join(DATA_DIR, 'models/')
LOG_DIR = 'logs/'
