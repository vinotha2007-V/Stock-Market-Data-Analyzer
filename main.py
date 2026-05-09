from src.fetch_data import get_stock_data
from src.indicators import add_indicators
from src.visualization import plot_stock
from src.prediction import train_model

def main():

    ticker = input("Enter Stock Ticker: ")

    df = get_stock_data(ticker)

    df = add_indicators(df)

    print(df.tail())

    plot_stock(df)

    train_model(df)

if __name__ == "__main__":
    main()
