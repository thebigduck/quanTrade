# src/backtester.py

import backtrader as bt
import matplotlib
from matplotlib import pyplot as plt

def run_backtest(data, strategy, **kwargs):
    """
    Runs a backtest on the given data using the specified strategy.
    Returns the matplotlib figure object containing the plot.
    """
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy, **kwargs)

    # Create a Data Feed
    data_feed = bt.feeds.PandasData(
        dataname=data,
        datetime=None,
        open='open',
        high='high',
        low='low',
        close='adj close',  # Use adjusted close prices as 'close'
        volume='volume',
        openinterest=-1
    )
    cerebro.adddata(data_feed)

    cerebro.broker.set_cash(100000.0)
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")

    # Suppress plt.show()
    original_show = plt.show
    plt.show = lambda *args, **kwargs: None  # Replace plt.show() with a no-op

    # Plotting
    matplotlib.use('Agg')  # Use non-interactive backend
    figures = cerebro.plot(
        style='candlestick',
        figsize=(12, 8),
        show=False  # This might be ignored, so we suppress plt.show()
    )
    fig = figures[0][0]  # Get the first figure

    # Restore plt.show()
    plt.show = original_show
    return fig
