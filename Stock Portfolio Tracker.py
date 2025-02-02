# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R-68mi-U2COuMxBI5e0G74LIgeXiP2W-
"""

# Install yfinance
!pip install yfinance

import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares}
        print(f'Added {shares} shares of {symbol}.')

    def remove_stock(self, symbol, shares):
        """Remove stock from the portfolio."""
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] >= shares:
                self.portfolio[symbol]['shares'] -= shares
                print(f'Removed {shares} shares of {symbol}.')
                if self.portfolio[symbol]['shares'] == 0:
                    del self.portfolio[symbol]
            else:
                print(f'Not enough shares of {symbol} to remove.')
        else:
            print(f'{symbol} not found in portfolio.')

    def get_stock_prices(self):
        """Fetch current stock prices for all stocks in the portfolio."""
        symbols = list(self.portfolio.keys())
        prices = yf.download(symbols)['Close'].iloc[-1]
        return prices.to_dict()

    def track_performance(self):
        """Track and display the performance of the portfolio."""
        total_investment = 0
        total_value = 0

        prices = self.get_stock_prices()

        for symbol, info in self.portfolio.items():
            shares = info['shares']
            price = prices.get(symbol, None)
            if price is not None:
                value = shares * price
                total_investment += shares * 100  # Assume each share was bought at $100 for simplicity
                total_value += value
                print(f'{symbol}: {shares} shares, Current Price: ${price:.2f}, Value: ${value:.2f}')
            else:
                print(f'Price for {symbol} not found.')

        print(f'Total Investment: ${total_investment:.2f}')
        print(f'Total Value: ${total_value:.2f}')
        print(f'Portfolio Gain/Loss: ${total_value - total_investment:.2f}')

# Example usage
if __name__ == '__main__':
    portfolio = StockPortfolio()

    # Example inputs
    portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
    portfolio.add_stock('MSFT', 5)    # Add 5 shares of Microsoft
    portfolio.remove_stock('AAPL', 3)  # Remove 3 shares of Apple

    # Track the performance of the portfolio
    portfolio.track_performance()