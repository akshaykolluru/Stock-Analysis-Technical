import yfinance as yf
import pandas as pd
msft = yf.Ticker("MSFT")
info = msft.info
print(info.get("sector"))