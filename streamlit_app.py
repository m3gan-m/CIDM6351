# To turn this app,
# 0. Make a copy (Fork) of this repl with your repl account
# 1. install required packages in Shell:  pip install streamlit yfinance mysql-connector-python plotly
# 2. type  streamlit run streamlit_app.py  within the Shell

# import packages needed
from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.express as px
import mysql.connector
import pandas as pd

# print title
st.title("CIDM6351 Streamlit Homework 10")
# print plain text
st.write(
    "Your Name: Megan Moore")
st.write(
    "Your email: mmmoore2@buffs.wtamu.edu")
st.write(
    "___________________________________________________________"
)

# print text formatted by HTML
#st.markdown("<h1 style='text-align:center; color:red;'> Sample Stock Price App. </h1>", unsafe_allow_html=True)


# print text in markdown
st.markdown("## **Check Stock Information**")

# a list of stock names
stock_names = ['MSFT', 'AAPL', 'AMZN', 'GOOGL']
# select a stock to check
target_stock = st.multiselect("Choose at least TWO stocks to visualize. Default stocks: AAPL, NFLX", stock_names,['AAPL','MSFT'])
#target_stock = st.selectbox('Select a stock to check', options=stock_names)
#multitarget_stock = st.multiselect('Select a stock to check', ['MSFT','AAPL']) 

st.markdown("## **Check Stock Price History**")

# start date of the stock infomation, default is the first day of year 2021
start_date = st.date_input('Start Date', datetime(2021, 1, 1))
# end date of the stock infomation, default is date of today
end_date = st.date_input("End Date")

# get today date
today = date.today()
if st.button('Submit'):
    # check valid date
    if start_date > today or end_date > today:
        st.write("## **Please select a valid date period. **")
    else:
        # download the stock data based on stock name, start/end date
        data = yf.download(tickers=target_stock,start=start_date,end=end_date)
        # show a progress bar
        with st.spinner(text='In progress'):
            high = data['High']
            fig = px.line(high,
                          x=high.index,
                          y=list(high.columns),
                          title=f"High Stock Price:{start_date} to {end_date}",
                          labels={
                              "value": "Stock Price ($)",
                              "variable": "Stock"
                          })
            st.write(fig)
            st.success('Done')
