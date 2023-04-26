# Fundamental Analysis with Yahoo Finance and Python

<div>This program is a Python implementation of fundamental analysis using financial data from Yahoo Finance. It includes a class called FundamentalAnalysis that can be used to perform fundamental analysis on a stock using historical stock price data from Yahoo Finance.</div>

## Getting Started

<div>To use this program, you will need to install Python and the required Python packages. You can install the required packages using the following command:</div>

``` python

pip install -r requirements.txt

```

<div>
You can then run the program using the following command:
</div>

``` bash

python main.py

```

<div>
By default, the program will perform fundamental analysis on Apple Inc. (AAPL). You can specify a different stock symbol by passing the stock symbol as a command line argument, like this:
</div>


``` bash

python main.py

```




# Class Usage

To use the FundamentalAnalysis class in your own Python programs, you can import the class from the FundamentalAnalysis.py file, like this:

``` python
from FundamentalAnalysis import FundamentalAnalysis

# Create a FundamentalAnalysis object for a stock
fa = FundamentalAnalysis('AAPL')

# Clean and process the data
fa.clean_data()

# Analyze the data
metrics = fa.analyze_data()
print(metrics)

# Create visualizations
fa.visualize_data()
```

<div>
This will create a FundamentalAnalysis object for Apple Inc. (AAPL), clean and process the data, analyze the data, and create visualizations.
</div>

# Docker Usage

<div>
You can also use Docker to run the FundamentalAnalysis program in a containerized environment. To do this, you can build a Docker image using the provided Dockerfile, like this:
</div>

``` bash
docker build -t fundamental_analysis .
```


You can then run the Docker container using the following command:


``` bash

docker run -it -e STOCK_NAME=AAPL fundamental_analysis

```

<div>
This will build the Docker image and run the FundamentalAnalysis program for Apple Inc. (AAPL) inside the Docker container. You can specify a different stock symbol by changing the value of the STOCK_NAME environment variable.
</div>
