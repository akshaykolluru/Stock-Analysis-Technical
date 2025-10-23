import pandas as pd
import matplotlib.pyplot as plt

# Read CSV and skip extra ^GSPC row
df = pd.read_csv("GSPC_OHLCV.csv", skiprows=[1])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Daily percent change
df['Daily_Return'] = df['Close'].pct_change() * 100

# Compute mean and std
mean = df['Daily_Return'].mean()
std = df['Daily_Return'].std()

# Flag anomalies
df['Anomaly'] = (df['Daily_Return'] > mean + 2*std) | (df['Daily_Return'] < mean - 2*std)

# Replace anomalies with rolling 5-day mean
df['Close_fixed'] = df['Close']
df.loc[df['Anomaly'], 'Close_fixed'] = df['Close'].rolling(window=5, center=True).mean()

# Plot original vs fixed
plt.figure(figsize=(14,7))
plt.plot(df['Close'], label='Original Close', color='blue', alpha=0.5)
plt.plot(df['Close_fixed'], label='Fixed Close', color='orange')
plt.title('S&P 500 Close Price: Original vs Fixed')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()