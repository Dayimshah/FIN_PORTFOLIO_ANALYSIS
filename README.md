# Portfolio Simulation using NumPy, Pandas, and yFinance

This project simulates random investment portfolios using historical stock data fetched with the `yfinance` library. It calculates expected annual returns and risks (volatility) for each portfolio based on weighted allocations to different stocks.

---

## Features

- Downloads historical stock price data for multiple tickers.
- Calculates daily returns and covariances.
- Simulates thousands of random portfolios with different weight combinations.
- Calculates expected annual returns and portfolio volatility (risk).
- Prints sample portfolios with their weights, returns, and risks.
- Includes a scatter plot visualizing the risk-return tradeoff across simulated portfolios.

---

## Technologies Used

- Python 3.x
- NumPy
- Pandas
- yFinance
- Matplotlib

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio-simulation.git
   cd portfolio-simulation
