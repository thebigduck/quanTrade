# app.py

import streamlit as st
from src.data_fetcher import fetch_order_book_data, fetch_historical_data
from src.indicators import (
    calculate_total_sell_volume,
    calculate_sell_to_buy_ratio,
    calculate_order_book_imbalance,
)
from src.models.stock_growth_predictor import predict_growth_potential
from src.visualizer import plot_order_book_depth, plot_backtest_results
from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY
from src.backtester import run_backtest

# Set page configuration
st.set_page_config(page_title="Stock Value Growth Predictor", layout="wide")

# Title
st.title("Stock Value Growth Predictor and Backtester")

# API Key Check
if not ALPACA_API_KEY or not ALPACA_SECRET_KEY:
    st.error("API keys are not set. Please configure them in the environment variables.")
else:
    # User Input
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)")

    if st.button("Analyze"):
        if ticker:
            # Fetch Order Book Data
            order_book_data = fetch_order_book_data(ticker)
            if order_book_data:
                # Calculate Indicators
                total_sell_volume = calculate_total_sell_volume(order_book_data)
                sell_to_buy_ratio = calculate_sell_to_buy_ratio(order_book_data)
                order_book_imbalance = calculate_order_book_imbalance(order_book_data)

                # Display Indicators
                st.subheader("Order Book Indicators")
                st.write(f"Total Sell Volume (Top Levels): {total_sell_volume}")
                st.write(f"Sell-to-Buy Volume Ratio: {sell_to_buy_ratio:.2f}")
                st.write(f"Order Book Imbalance: {order_book_imbalance:.2f}")

                # Prediction
                prediction, probability = predict_growth_potential(order_book_data)
                if prediction == 1:
                    st.success(
                        f"{ticker.upper()} has **high growth potential** with a confidence of {probability:.2%}"
                    )
                else:
                    st.info(f"{ticker.upper()} does not show high growth potential.")

                # Visualization
                st.subheader("Order Book Depth")
                fig = plot_order_book_depth(order_book_data)
                st.pyplot(fig)

                # Option to Run Backtest
                if st.button("Run Backtest"):
                    st.subheader("Backtesting Results")
                    backtest_results = run_backtest(ticker)
                    if backtest_results:
                        st.write(f"Total Return: {backtest_results['total_return']:.2%}")
                        st.write(f"Sharpe Ratio: {backtest_results['sharpe_ratio']:.2f}")
                        st.write(f"Max Drawdown: {backtest_results['max_drawdown']:.2%}")
                        # Plot equity curve
                        equity_fig = plot_backtest_results(backtest_results['equity_curve'])
                        st.pyplot(equity_fig)
                    else:
                        st.error("Backtest failed. Please check the logs for more information.")

            else:
                st.error(f"Failed to retrieve data for {ticker.upper()}.")
        else:
            st.error("Please enter a stock ticker.")
