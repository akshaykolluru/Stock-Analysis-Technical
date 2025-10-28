import pandas as pd
import pandas_ta as ta
import glob

files = glob.glob("../data/*_OHLCV.csv")

for file in files:
    print(f"\nProcessing {file.split('/')[-1]}")
    df = pd.read_csv(file)
    df.set_index('Date', inplace=True)

    # Ensure numeric columns
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Disable numba usage by ensuring numpy-only functions
    df['SMA_20'] = df['Close'].rolling(20).mean()
    df['SMA_50'] = df['Close'].rolling(50).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['RSI'] = ta.rsi(df['Close'], length=14, append=False)
    df['MACD'] = ta.macd(df['Close'], append=False)['MACD_12_26_9']
    df['Signal_Line'] = ta.macd(df['Close'], append=False)['MACDs_12_26_9']

    bbands = ta.bbands(df['Close'], length=20)
    df['BB_upper'] = bbands['BBU_20_2.0']
    df['BB_middle'] = bbands['BBM_20_2.0']
    df['BB_lower'] = bbands['BBL_20_2.0']

    df['OBV'] = ta.obv(df['Close'], df['Volume'])

    df.dropna(inplace=True)
    output_file = file.replace("_OHLCV.csv", "_TA.csv")
    df.to_csv(output_file)
    print(f"✅ Saved indicators to {output_file}")

print("\n🎯 All indicators generated successfully without numba.")