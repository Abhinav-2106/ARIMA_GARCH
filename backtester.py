from backtesting import Backtest, Strategy
class ARIMAGARCHStrategy(Strategy):
    sl_mult = 1.0
    tp_mult = 2.0
    def init(self):
        pass
    def next(self):
        signal = self.data.Signal[-1]
        volatility = self.data.Volatility[-1]
        price = self.data.Close[-1]
        sl_distance = price * volatility * self.sl_mult
        tp_distance = price * volatility * self.tp_mult
        if signal == 1 and not self.position:
            sl = price - sl_distance
            tp = price + tp_distance
            self.buy(sl=sl, tp=tp)

        elif signal == -1 and not self.position:
            sl = price + sl_distance
            tp = price - tp_distance
            self.sell(sl=sl, tp=tp)