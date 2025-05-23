import yfinance as yf

def fetch_data(ticker="AAPL", start="2015-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    return df
