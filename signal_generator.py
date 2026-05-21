import numpy as np

def generate_signals(df, arima_forecasts, garch_forecasts, window):

    df = df.iloc[window:].copy()

    df["ARIMA_Forecast"] = arima_forecasts
    df["Volatility"] = garch_forecasts

    signals = []

    threshold = 0.006
    median_volatility = df["Volatility"].median()
    low_vol = median_volatility * 0.5
    high_vol = median_volatility * 1.5

    for i in range(len(df)):

        forecast = df["ARIMA_Forecast"].iloc[i]
        volatility = df["Volatility"].iloc[i]
        rsi = df["RSI"].iloc[i]
        sma50 = df["SMA50"].iloc[i]
        sma200 = df["SMA200"].iloc[i]

        if np.isnan(rsi) or np.isnan(sma50) or np.isnan(sma200):
            signals.append(0)
            continue

        signal = 0

        bullish_trend = sma50 > sma200
        bearish_trend = sma50 < sma200

        if (
            forecast > threshold
            and bullish_trend
            and volatility < high_vol
        ):
            signal = 1

        elif (
            forecast < -threshold
            and bearish_trend
            and  volatility < high_vol
        ):
            signal = -1

        signals.append(signal)

    print(len(signals))
    print(len(df))

    df["Signal"] = signals

    return df