import pandas as pd
import matplotlib.pyplot as plt

# Read CSV and skip the extra ^GSPC row
df = pd.read_csv("GSPC_OHLCV.csv", skiprows=[1])

# Convert 'Date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate 20-day moving average for Close price
df['MA_20'] = df['Close'].rolling(window=20).mean()

# Plot Close, High, Low, and Moving Average
plt.figure(figsize=(14,7))
plt.plot(df['Close'], label='Close', color='blue')
plt.plot(df['High'], label='High', color='green', alpha=0.5)
plt.plot(df['Low'], label='Low', color='red', alpha=0.5)
plt.plot(df['MA_20'], label='20-day MA', color='orange', linestyle='--')
plt.title('S&P 500 Prices with 20-day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.savefig("GSPC_graph.ipynb")