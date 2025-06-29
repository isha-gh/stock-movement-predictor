# src/data_loader.py
import yfinance as yf 
import pandas as pd
import os
def download_stock_data(ticker='AAPL', start='2018-01-01', end='2024-01-01'):
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    df.reset_index(inplace=True)
    # Flatten multi-level columns if they exist:
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)  # take the last level only
    # Select just these columns
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    return df

def load_clean_stock_data(csv_path='data/raw/AAPL_prices.csv'):
    # Skip second row because it contains ticker label, not data
    df = pd.read_csv(csv_path, skiprows=[1])

    # Convert numeric columns explicitly
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Optional: drop rows with missing values if any
    df.dropna(inplace=True)

    return df

if __name__ == "__main__":
    # Download and save raw data if not already saved
    if not os.path.exists('data/raw/AAPL_prices.csv'):
        os.makedirs('data/raw', exist_ok=True)
        df_raw = download_stock_data()
        df_raw.to_csv('data/raw/AAPL_prices.csv', index=False)
        print("Saved raw data.")

    # Load and clean data
    df_clean = load_clean_stock_data()
    print(df_clean.head())
    print(df_clean.info())