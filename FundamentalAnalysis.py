import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

class FundamentalAnalysis:
    def __init__(self, ticker):
        self.ticker = ticker
        self.ticker_data = yf.Ticker(ticker).history(period="max")
        
    def clean_data(self):
        # Calculate daily returns
        self.ticker_data['daily_returns'] = self.ticker_data['Close'].pct_change()
        
    def analyze_data(self):
        # Calculate P/E ratio
        pe_ratio = self.ticker_data['Close'].mean() / self.ticker_data['Close'].mean()
        
        # Calculate P/B ratio
        pb_ratio = self.ticker_data['Close'].mean() / self.ticker_data['Close'].mean()
        
        # Calculate dividend yield
        dividend_yield = self.ticker_data['Dividends'].sum() / self.ticker_data['Close'].iloc[-1]
        
        return {'P/E Ratio': pe_ratio, 'P/B Ratio': pb_ratio, 'Dividend Yield': dividend_yield}
    
    def visualize_data(self):
        # Create line chart of daily returns
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=self.ticker_data.index, y=self.ticker_data['daily_returns'])
        plt.title(f'Daily Returns for {self.ticker}')
        plt.ylabel('Daily Returns')
        plt.show()
