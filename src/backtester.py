# src/backtester.py

import backtrader as bt

def run_backtest(data, strategy, **kwargs):
    """
    Runs a backtest on the given data using the specified strategy.
    """
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy, **kwargs)


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
    cerebro.plot()
