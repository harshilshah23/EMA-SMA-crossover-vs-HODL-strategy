import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# List of five stocks from the S&P500 index
stocks = ["AAPL", "MSFT", "AMZN", "GOOGL", "JPM"]

# Fetch data from Yahoo Finance for the specified period
start_date = "2000-01-01"
end_date = "2024-01-01"

data = {}
for stock in stocks:
    data[stock] = yf.download(stock, start=start_date, end=end_date)

# Define the strategy parameters
short_ema_window = 20  # Short-term EMA window
long_sma_window = 100  # Long-term SMA window
stop_loss_percentage = 0.05  # Stop-loss percentage
initial_investment = 1000  # Initial investment amount

# Backtest the strategy
for stock, df in data.items():
    df["Short_EMA"] = df["Adj Close"].ewm(span=short_ema_window, adjust=False).mean()
    df["Long_SMA"] = df["Adj Close"].rolling(window=long_sma_window).mean()

    # Generate signals
    df["Signal"] = 0.0
    df.loc[df["Short_EMA"] > df["Long_SMA"], "Signal"] = 1.0  # Buy signal
    df.loc[df["Short_EMA"] < df["Long_SMA"], "Signal"] = -1.0  # Sell signal

    # Calculate the strategy returns
    df["Returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Strategy_Returns"] = df["Signal"].shift(1) * df["Returns"]

    # Implement stop-loss
    stop_loss_condition = df["Strategy_Returns"].cumsum() < -stop_loss_percentage
    df.loc[stop_loss_condition, "Strategy_Returns"] = 0

    # Calculate performance metrics
    strategy_return = df["Strategy_Returns"].sum()
    buy_and_hold_return = (df["Adj Close"].iloc[-1] / df["Adj Close"].iloc[0]) - 1
    epsilon = 1e-8  # A small positive value
    sharpe_ratio = df["Strategy_Returns"].mean() / (pd.Series(df["Strategy_Returns"].std()) + epsilon) * np.sqrt(252)
    max_drawdown = np.max(np.maximum.accumulate(df["Strategy_Returns"]) - df["Strategy_Returns"])

    # Calculate final portfolio value
    final_portfolio_value = initial_investment * np.exp(strategy_return)
    df["Portfolio_Value"] = initial_investment * np.exp(df["Strategy_Returns"].cumsum())

    print(f"{stock} Strategy Return: {strategy_return:.2%}")
    print(f"{stock} Buy and Hold Return: {buy_and_hold_return:.2%}")
    print(f"{stock} Sharpe Ratio: {sharpe_ratio.iloc[0]:.2f}")
    print(f"{stock} Max Drawdown: {max_drawdown:.2%}")
    print(f"{stock} Final Portfolio Value: ${final_portfolio_value:.2f}")
    print("-" * 30)

    # Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Adj Close"], label="Adjusted Close")
    plt.plot(df.index, df["Portfolio_Value"], label="Portfolio Value")
    plt.plot(df.index, df["Short_EMA"], label="Short EMA")
    plt.plot(df.index, df["Long_SMA"], label="Long SMA")
    plt.scatter(df.index[df["Signal"] == 1], df["Adj Close"][df["Signal"] == 1], marker="^", color="green", label="Buy Signal", s=100)
    plt.scatter(df.index[df["Signal"] == -1], df["Adj Close"][df["Signal"] == -1], marker="v", color="red", label="Sell Signal", s=100)
    plt.title(f"{stock} Trend-Following Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


