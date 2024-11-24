# src/strategies/sma_crossover.py

import backtrader as bt

class SmaCrossoverStrategy(bt.Strategy):
    params = dict(
        pfast=10,  # Period for the fast moving average
        pslow=30   # Period for the slow moving average
    )

    def __init__(self):
        sma_fast = bt.ind.SMA(period=self.p.pfast)
        sma_slow = bt.ind.SMA(period=self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma_fast, sma_slow)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.sell()
