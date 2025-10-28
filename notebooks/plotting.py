import pandas as pd
import matplotlib.pyplot as plt

# Read CSV (same as before)
df = pd.read_csv("GSPC_OHLCV.csv", skiprows=[1])

# Convert 'Date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Plot Price and Volume
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Close Price
ax1.plot(df['Close'], color='blue', label='Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second axis for Volume
ax2 = ax1.twinx()
ax2.bar(df.index, df['Volume'], color='gray', alpha=0.3, label='Volume')
ax2.set_ylabel('Volume', color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

# Title and Legend
plt.title('S&P 500 — Price vs Volume')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.show()