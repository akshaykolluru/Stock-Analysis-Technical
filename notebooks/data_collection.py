import yfinance as yf
import pandas as pd

tickers = ["AAPL", "TATAMOTORS.NS", "^GSPC"]
start_date = "2019-01-01"
end_date = "2024-12-31"

for ticker in tickers:
    print(f"Downloading {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    data.dropna(inplace=True)
    filename = f"../data/{ticker.replace('.', '_').replace('^', '')}_OHLCV.csv"
    data.to_csv(filename)
    print(f"✅ Saved {filename}")

print("\nAll stock data downloaded successfully!")