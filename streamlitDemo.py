# To turn this app,
# 0. Make a copy (Fork) of this repl with your repl account
# 1. install required packages in Shell:  pip install streamlit yfinance mysql-connector-python plotly
# 2. type  streamlit run streamlit_app.py  within the Shell

get-pip.py
#pip install -r requirements.txt

# import packages needed
from datetime import date, datetime
import streamlit as st
import yfinance as yf

import plotly.express as px
import mysql.connector
import pandas as pd

# print title
st.title("CIDM6351 Streamlit Demo")
# print plain text
st.write(
    "**Streamlit**: The fastest way to build and share data apps in Python")
st.write(
    "Here is the cheat sheet of Streamlit. It summarized features of Streamlit: https://docs.streamlit.io/library/cheatsheet#display-progress-and-status"
)

# print text formatted by HTML
st.markdown(
    "<h1 style='text-align:center; color:red;'> Sample Stock Price App. </h1>",
    unsafe_allow_html=True)

st.write(
    'We will use the code learned from previous lecture to build an online application for tracing stock price'
)

# print text in markdown
st.markdown("## **Check Stock Information**")

# a list of stock names
stock_names = ['MSFT', 'AAPL', 'AMZN', 'GOOGL']
# select a stock to check
target_stock = st.selectbox('Select a stock to check', options=stock_names)

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
        st.write("## **Please select a valid date period.**")
    else:
        # download the stock data based on stock name, start/end date
        data = yf.download(target_stock, start_date, end_date)
        # show a progress bar
        with st.spinner(text='In progress'):

            fig = px.line(data,
                          x=data.index,
                          y=['Open', 'High', 'Low', 'Close'],
                          title=target_stock + " Stock Price",
                          labels={
                              "value": "Stock Price ($)",
                              "variable": "Price Type"
                          })
            st.write(fig)
            st.success('Done')

st.markdown(
    "<h1 style='text-align:center; color:red;'> Show Data From Database </h1>",
    unsafe_allow_html=True)

# Define MySQL Connection String
cnx = mysql.connector.connect(
    user='cidm6351',  # username of database
    password='dataETL@WT',  # password of database
    host='20.172.0.16',  # ip address of the database
    database='cidm6351',  # target database 
    port=8080  # the default port of MySQL is 3306.     
)

if st.button('See All Patients Records'):

    query = "SELECT * FROM patients"
    # use pandas to query records
    df = pd.read_sql(query, cnx)
    st.dataframe(df)
