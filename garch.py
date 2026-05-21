from arch import arch_model

def rolling_garch_forecast(returns, window):
    vol_forecasts = []
    for i in range(window, len(returns)):
        train = returns[i-window:i]
        model = arch_model(
            train,
            vol="Garch",
            p=1,
            q=1,
            mean ="Zero"
        )
        fitted = model.fit(disp="off",show_warning=False)
        forecast = fitted.forecast(horizon=1)
        variance = forecast.variance.values[-1,0]
        volatility = variance ** 0.5
        vol_forecasts.append(volatility)
    return vol_forecasts