import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
DEFAULT_TICKER = os.getenv('DEFAULT_TICKER', 'AAPL')
START_DATE = os.getenv('START_DATE', '2020-01-01')
END_DATE = os.getenv('END_DATE', '2021-01-01')
