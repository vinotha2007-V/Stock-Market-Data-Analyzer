import streamlit as st
from src.fetch_data import get_stock_data
from src.indicators import add_indicators
import plotly.graph_objects as go

st.title("📈 Stock Market Data Analyzer")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

df = get_stock_data(ticker)

df = add_indicators(df)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Close'],
    mode='lines',
    name='Close Price'
))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['SMA_20'],
    mode='lines',
    name='SMA 20'
))

st.plotly_chart(fig)

st.dataframe(df.tail())
