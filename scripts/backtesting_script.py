# scripts/backtest_script.py

from src.backtester import run_backtest

if __name__ == "__main__":
    ticker = "AAPL"
    results = run_backtest(ticker, start_date="2020-01-01", end_date="2020-12-31")
    if results:
        print(f"Total Return: {results['total_return']:.2%}")
        print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
        print(f"Max Drawdown: {results['max_drawdown']:.2%}")
    else:
        print("Backtest failed.")
