# src/backtester.py

import backtrader as bt 

def run_backtest(data, strategy, **kwargs):
    """
    Runs a backtest on the given data using the specified strategy.
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
        close='close',
        volume='volume',
        openinterest=-1,
        adjclose='adj close'  # Include if using adjusted close prices
    )
    cerebro.adddata(data_feed)

    cerebro.broker.set_cash(100000.0)
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.plot()
