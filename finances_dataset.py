import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']

data = yf.download(tickers, start='2020-01-01', end='2024-12-31')

# Use 'Close' instead of 'Adj Close'
adj_close = data.loc[:, ('Close', slice(None))]
adj_close.columns = adj_close.columns.droplevel(0)  # Now columns are tickers only

returns = adj_close.pct_change().dropna()

num_portfolios = 5000
all_weights = np.zeros((num_portfolios, len(tickers)))
portfolio_returns = np.zeros(num_portfolios)
portfolio_volatility = np.zeros(num_portfolios)

mean_returns = returns.mean()
cov_matrix = returns.cov()

for i in range(num_portfolios):
    weights = np.random.random(len(tickers))
    weights /= np.sum(weights)
    all_weights[i, :] = weights
    
    port_return = np.sum(mean_returns * weights) * 252
    portfolio_returns[i] = port_return
    
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    portfolio_volatility[i] = port_vol

for i in range(5):
    print(f"Portfolio {i+1}:")
    for ticker, weight in zip(tickers, all_weights[i]):
        print(f"  {ticker}: {weight:.2%}")
    print(f"  Expected Annual Return: {portfolio_returns[i]:.2%}")
    print(f"  Expected Annual Volatility (Risk): {portfolio_volatility[i]:.2%}")
    print()


plt.figure(figsize=(10,6))
plt.scatter(portfolio_volatility, portfolio_returns, c=portfolio_returns/portfolio_volatility, marker='o', cmap='viridis')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe Ratio (Return/Risk)')
plt.title('Simulated Portfolios: Risk vs Return')
plt.show()

