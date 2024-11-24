import requests

def fetch_alpaca_order_book(ticker, api_key, api_secret):
    base_url = 'https://api.alpaca.markets'
    endpoint = f'/{ticker}/quotes/latest'
    headers = {
        'APCA-API-KEY-ID': api_key,
        'APCA-API-SECRET-KEY': api_secret
    }
    response = requests.get(base_url + endpoint, headers=headers)
    data = response.json()
    return data
