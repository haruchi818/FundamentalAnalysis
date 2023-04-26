# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FundamentalAnalysis class file
COPY FundamentalAnalysis.py .

# Copy the main program file
COPY main.py .

# Set the environment variable for the stock name
ENV STOCK_NAME AAPL

# Run the main program with the environment variable
CMD ["python", "main.py"]
