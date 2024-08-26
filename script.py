import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('sample_orders.csv')
st.write(df)

st.line_chart(df[['Date', 'Order Value']].set_index('Date'))
st.bar_chart(df[['Order Category', 'Order Value']].groupby('Order Category').sum())
st.area_chart(df[['Date', 'Order Value']].set_index('Date'))
fig = px.bar(df, x='Order Category', y='Order Value', title='Sales by Product Category')
st.plotly_chart(fig)

