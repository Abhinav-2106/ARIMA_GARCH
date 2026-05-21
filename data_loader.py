import yfinance as yf
def download_data(ticker="KO", start="2019-01-01", end = "2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    df.columns = df.columns.droplevel(1)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df.dropna(inplace=True)
    return df
