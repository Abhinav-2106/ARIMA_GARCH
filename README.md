# ARIMA_GARCH
ARIMA-GARCH Trading Signal Generator

This project implements a quantitative trading strategy using:

ARIMA for short-term return forecasting
GARCH for volatility forecasting and dynamic risk management
Technical Indicators (RSI, SMA50, SMA200) for trade filtering
Backtesting.py for historical strategy evaluation
TA-Lib for indicator computation
Strategy Logic
1. ARIMA Forecasting

ARIMA is used on rolling windows of log returns to predict the next day's return direction.

Positive forecast → bullish expectation
Negative forecast → bearish expectation

A threshold is used to avoid trading on weak/noisy forecasts.

2. GARCH Volatility Modeling

GARCH forecasts future volatility using rolling windows.

Predicted volatility is used to dynamically set:

Stop-loss levels
Take-profit levels

This creates adaptive risk management instead of fixed percentage exits.

3. Technical Filters

The strategy also uses:

RSI for momentum filtering
SMA50 and SMA200 for trend confirmation

Example:

Buy only in bullish long-term trends
Sell only in bearish trends
Backtesting

The strategy is evaluated using:

Return %
Sharpe Ratio
Drawdown
Trade statistics
Buy-and-Hold comparison

Assets tested:

KO
AAPL
BTC-USD


Key Learnings
Financial markets are highly noisy and difficult to predict.
Small ARIMA forecasts often behave like random noise.
Threshold filtering significantly improves signal quality.
Volatility regime filtering can reduce poor trades.
Buy-and-hold is extremely difficult to outperform during strong bull markets.
Risk management and filtering are as important as prediction models.
Tech Stack
Python
pandas
numpy
statsmodels
arch
yfinance
TA-Lib
backtesting.py
matplotlib
