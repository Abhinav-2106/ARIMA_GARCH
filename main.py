import warnings

from statsmodels.tools.sm_exceptions import (
    ConvergenceWarning,
    ValueWarning
)

warnings.simplefilter("ignore", FutureWarning)
warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", RuntimeWarning)
warnings.simplefilter("ignore", ConvergenceWarning)
warnings.simplefilter("ignore", ValueWarning)

from data_loader import download_data
from pre_processing import compute_log_returns, adf_test
from indicator import add_indicators
from arima_model import rolling_arima_forecast
from garch import rolling_garch_forecast
from signal_generator import generate_signals
from backtester import ARIMAGARCHStrategy

from backtesting import Backtest

window = 252
df = download_data(
    ticker = "KO",
    start="2019-01-01",
    end= "2024-01-01"
)
df = compute_log_returns(df)
adf_test(df["Returns"])
df = add_indicators(df)
arima_forecasts = rolling_arima_forecast(
    df["Returns"],
    window
)
garch_forecasts = rolling_garch_forecast(
    df["Returns"],
    window
)
df = generate_signals(
    df,
    arima_forecasts,
    garch_forecasts,
    window)
df.dropna(inplace=True)
bt = Backtest(
    df,
    ARIMAGARCHStrategy,
    cash=100000,
    commission=0.002,
    exclusive_orders=True
)
stats = bt.run()
print(stats)
bt.plot()
