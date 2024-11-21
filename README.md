# Quantitaive Trading App MVP

## Overview

This repository contains the source code for a **Quantitative Trading Application MVP (Minimum Viable Product)** built with Python. The application provides a platform for fetching historical stock data, implementing trading strategies, running backtests, and visualizing results through an interactive web interface powered by Streamlit.

## Features

- **Data Fetching**: Retrieve historical stock data using the `yfinance` library.
- **Data Processing**: Clean and preprocess data for accurate analysis.
- **Trading Strategies**: Implemented a Simple Moving Average (SMA) Crossover strategy.
- **Backtesting Module**: Simulate trading strategies on historical data using Backtrader.
- **Visualization**: Generate interactive plots for stock prices and backtesting performance.
- **Web Interface**: User-friendly interface built with Streamlit for easy interaction.

## Project Structure

```
quant_trading_app/
├── app.py                   # Main application file (Streamlit app)
├── requirements.txt         # Python dependencies
├── README.md                # Project description
├── src/
│   ├── __init__.py          # Makes 'src' a Python package
│   ├── config.py            # Configuration variables and settings
│   ├── data_fetcher.py      # Functions to fetch stock data
│   ├── data_processor.py    # Functions to preprocess data
│   ├── backtester.py        # Module to run backtests
│   ├── visualizer.py        # Functions to visualize data and results
│   └── strategies/
│       ├── __init__.py      # Makes 'strategies' a Python package
│       └── sma_crossover.py # SMA Crossover strategy implementation
└── tests/
    ├── __init__.py          # Makes 'tests' a Python package
    ├── test_data_fetcher.py # Tests for data fetching functions
    ├── test_data_processor.py # Tests for data processing functions
    ├── test_strategies.py   # Tests for trading strategies
    └── test_backtester.py   # Tests for the backtesting module
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/quant_trading_app.git
   cd quant_trading_app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   - Create a `.env` file in the root directory with the following content:

     ```
     API_KEY=your_api_key_here
     DEFAULT_TICKER=AAPL
     START_DATE=2020-01-01
     END_DATE=2021-01-01
     ```

   - Replace `your_api_key_here` with your actual API key if required.

## Usage

1. **Run the Application**

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Application**

   - Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.
   - **Enter Stock Ticker**: Input the stock symbol (e.g., `AAPL`).
   - **Select Date Range**: Choose the start and end dates for historical data.
   - **Fetch Data**: Click the "Fetch Data" button to retrieve and display stock data.
   - **Run Backtest**: Click the "Run Backtest" button to execute the SMA Crossover strategy and view the results.

## Testing

Run unit tests to ensure that each module is working correctly:

```bash
python -m unittest discover tests
```

## Configuration

- **Default Settings**: Adjust default settings in `src/config.py` or via the `.env` file.
- **Strategies**: Add new strategies in the `src/strategies/` directory following the existing structure.

## Features in Detail

### Data Fetching (`data_fetcher.py`)

- Uses `yfinance` to download historical stock data.
- Handles data cleaning and column formatting to ensure compatibility with other modules.

### Data Processing (`data_processor.py`)

- Preprocesses raw data by handling missing values and calculating returns.
- Ensures data integrity for accurate backtesting results.

### Trading Strategies (`strategies/`)

- **SMA Crossover Strategy (`sma_crossover.py`)**:
  - Implements a basic moving average crossover algorithm.
  - Generates buy/sell signals based on short-term and long-term moving averages.

### Backtesting (`backtester.py`)

- Integrates with Backtrader to simulate trading strategies on historical data.
- Provides performance metrics such as starting and ending portfolio values.

### Visualization (`visualizer.py`)

- Generates plots for stock prices and backtesting performance.
- Displays charts within the Streamlit app for interactive analysis.

## Future Enhancements

- **Additional Strategies**: Implement more complex trading algorithms.
- **Live Trading**: Integrate with brokerage APIs for real-time trading capabilities.
- **Database Integration**: Store historical data and backtesting results in a database.
- **Enhanced UI/UX**: Improve the web interface with advanced visualization tools.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Push the branch to your forked repository.
5. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgements

- **Backtrader**: For the backtesting framework.
- **yfinance**: For providing access to historical stock data.
- **Streamlit**: For the interactive web application framework.

