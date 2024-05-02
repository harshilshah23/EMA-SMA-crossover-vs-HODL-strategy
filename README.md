# EMA-SMA-crossover-vs-HODL-strategy
Trying out an algo trading bot that will calculate SMA + EMA crossover moves and compare and visualize it too buy and HODL strategy
#The strategy generates a buy signal (long position) when the short-term EMA (20 periods) crosses above the long-term SMA (100 periods).
#%The strategy generates a sell signal (short position or exit long position) when the short-term EMA crosses below the long-term SMA.
#Position Calculation:
#The strategy calculates the daily log returns.
#The buy/sell signals (1 for buy, -1 for sell) are shifted by one period and multiplied by the daily returns to obtain the strategy returns.
#Stop-Loss:
#The strategy implements a stop-loss mechanism to limit potential losses.
#If the cumulative strategy returns fall below a specified stop-loss percentage (set to -5% in the code), the position is closed, and the strategy returns for that day are set to 0.
#Performance Metrics:
#The strategy calculates various performance metrics:
#Strategy Return: The cumulative return of the strategy.
#Buy-and-Hold Return: The buy-and-hold return of the asset over the same period.
#Sharpe Ratio: The risk-adjusted return, calculated as the mean of strategy returns divided by the standard deviation of strategy returns, multiplied by the square root of 252 (assuming 252 trading days in a year).
#Maximum Drawdown: The maximum cumulative loss from a peak to a trough.
###The code plots the following elements for each stock:
#Adjusted Closing Prices: The historical adjusted closing prices of the stock.
#Portfolio Value: The portfolio value over time, starting with the initial investment amount and applying the cumulative strategy returns.
#Short-term EMA: The 20-period EMA line.
#@Long-term SMA: The 100-period SMA line.
#uy Signals: Green upward-pointing triangles indicating buy signal points.
#Sell Signals: Red downward-pointing triangles indicating sell signal points.///  */
