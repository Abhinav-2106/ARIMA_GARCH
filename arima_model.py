from statsmodels.tsa.arima.model import ARIMA

def rolling_arima_forecast(returns, window , order=(1,0,1)):
    forecasts = []
    for i in range(window, len(returns)):
        train = returns[i - window:i]
        model = ARIMA(train, order=order)
        fitted = model.fit()
        forecast = fitted.forecast().iloc[0]
        forecasts.append(forecast)
    return forecasts