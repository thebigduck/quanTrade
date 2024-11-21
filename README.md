# Instructions to Run the Application

## Clone the Repository

```sh
git clone https://github.com/your_username/quant_trading_app.git
cd quant_trading_app
```

## Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

## Install Dependencies

```sh
pip install -r requirements.txt
```

## Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```
API_KEY=your_api_key_here
DEFAULT_TICKER=AAPL
START_DATE=2020-01-01
END_DATE=2021-01-01
```

Replace `your_api_key_here` with your actual API key if required.

## Run the Application

```sh
streamlit run app.py
```

## Run Tests

```sh
python -m unittest discover tests
```

## Notes

- **API Keys**: For yfinance, no API key is needed. If you switch to an API that requires a key, make sure to update `data_fetcher.py` and store your API key securely.
- **Error Handling**: The code includes basic error handling. Consider adding more robust error checks for production.
- **Extensibility**: The structure allows for easy addition of new strategies and features.
- **Visualization**: Streamlit automatically handles the rendering of Matplotlib plots.
