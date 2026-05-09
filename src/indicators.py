import ta

def add_indicators(df):

    # Moving Average
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)

    # RSI
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)

    # MACD
    df['MACD'] = ta.trend.macd(df['Close'])

    return df
