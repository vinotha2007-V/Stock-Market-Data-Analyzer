import matplotlib.pyplot as plt

def plot_stock(df):

    plt.figure(figsize=(12,6))

    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20')

    plt.title("Stock Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()

    plt.show()
