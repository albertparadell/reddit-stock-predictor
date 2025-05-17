import yfinance as yf
import os

def fetch_stock_data(ticker, start_date="2020-01-01", end_date="2023-12-31", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance and save it as a CSV file.
    """
    print(f"🔄 Fetching data for {ticker}...")
    
    # Fetch the data
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

    # Create the data directory if it doesn't exist
    if not os.path.exists("data/stock"):
        os.makedirs("data/stock")
    
    # Use a consistent file naming format
    file_path = f"data/stock/{ticker}_{interval}_historical_data.csv"
    stock_data.to_csv(file_path)
    print(f"✅ Data for {ticker} saved to {file_path}")

    return stock_data

# Test the function
if __name__ == "__main__":
    fetch_stock_data("AAPL", interval="1d")
    fetch_stock_data("TSLA", interval="1d")
    fetch_stock_data("AMZN", interval="1wk")
