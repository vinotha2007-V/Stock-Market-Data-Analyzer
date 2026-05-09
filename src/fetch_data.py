import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL", period="1y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)

    df.reset_index(inplace=True)

    return df

if __name__ == "__main__":
    data = get_stock_data()
    print(data.head())
