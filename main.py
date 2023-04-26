import os
from FundamentalAnalysis import FundamentalAnalysis

# Get the stock name from the environment variable
stock_name = os.getenv('STOCK_NAME', 'AAPL')

# Create a FundamentalAnalysis object for the specified stock
fa = FundamentalAnalysis(stock_name)

# Clean and process the data
fa.clean_data()

# Analyze the data
metrics = fa.analyze_data()
print(metrics)

# Create visualizations
fa.visualize_data()