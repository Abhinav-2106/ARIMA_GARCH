import talib

def add_indicators(df):
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
    df["SMA50"] = talib.SMA(df["Close"], timeperiod=50)
    df["SMA200"] = talib.SMA(df["Close"], timeperiod=200)
    return df