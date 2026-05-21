import numpy as np
from statsmodels.tsa.stattools import adfuller
def compute_log_returns(df):
    df["Returns"] = np.log(df["Close"] / df["Close"].shift(1))
    df.dropna(inplace=True)
    return df
def adf_test(series):
    result = adfuller(series)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    
    if result[1]<0.05:
        print("Series is stationary")
    else:
        print("series is not stationary")
        

