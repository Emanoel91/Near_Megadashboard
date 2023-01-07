# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NEAR Price - Near Megadashboard', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🟠 NEAR Price')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/price2.JPG'))
with c2:
        st.subheader('📄 ***List of contents***')
        st.write(
                    """
                    1️⃣ **NEAR Price Overviw**
             
                    2️⃣ **USN Price Overview**
            
                    """
                )
               
# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# flipside API
@st.cache(ttl=600)
def get_data(query2):
    if query2 == 'NEAR Price per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/326e787e-b447-450a-8c2a-6ae94facc396/data/latest')
    elif query2 == 'Range of Price Changes':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6644dd6a-7aaf-4e0e-84d5-bd39f6a6c47c/data/latest')
    elif query2 == 'NEAR Price':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1c8db165-7910-4ded-b01b-21c65d831e48/data/latest')
    elif query2 == 'NEAR Price Metric':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9359a7c6-ab99-41f5-a87b-51ee140d8086/data/latest')
    elif query2 == 'USN Price per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ad7914c8-6f6a-48ba-9e04-51bc259f6dbf/data/latest')
    elif query2 == 'Amount of Price Changes Relative to the Peg Value':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9e04198-fff5-4ff4-9103-c8d24c0dc58a/data/latest')
    elif query2 == 'USN Price':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0006171a-78d9-4f49-b2b7-7bcd2ffddcc9/data/latest')
    return None

NEAR_Price_per_Day = get_data('NEAR Price per Day')
Range_of_Price_Changes = get_data('Range of Price Changes')
NEAR_Price = get_data('NEAR Price')
NEAR_Price_Metric = get_data('NEAR Price Metric')
USN_Price_per_Day = get_data('USN Price per Day')
Amount_of_Price_Changes_Relative_to_the_Peg_Value = get_data('Amount of Price Changes Relative to the Peg Value')
USN_Price = get_data('USN Price')

# NEAR Price Analysis
st.subheader('1️⃣ NEAR Price Overview')
c1 , c2 = st.columns(2)
c1.image(Image.open('Images/NEAR7.JPG'))

df = NEAR_Price_per_Day
fig = px.line(df, x='Date', y='Price', color='CRITERIA', title='NEAR Price per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = NEAR_Price_Metric
fig = px.line(df, x='Day', y='Price', color='TYPE', title='NEAR Price per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Range_of_Price_Changes

fig = px.bar(df, x='Date', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = NEAR_Price

c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='Current Price', value=df['Current Price'])
with c2:
        st.metric(label='ATH', value=df['ATH'])
with c3:
        st.metric(label='Max RoPC', value=df['Max RoPC']) 
        
# USN Price Analysis
st.subheader('2️⃣ USN Price Overview') 
c1 , c2 = st.columns(2)
c1.image(Image.open('Images/USN2.JPG'))

df = USN_Price_per_Day
fig = px.line(df, x='Date', y='Price', color='CRITERIA', title='USN Price per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Amount_of_Price_Changes_Relative_to_the_Peg_Value
fig = px.bar(df, x='Date', y='Price Changes', title='Amount of Price Changes Relative to the Peg Value', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = USN_Price
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='Current Price', value=df['Current Price'])
with c2:
        st.metric(label='Maximum Price', value=df['Maximum Price'])
with c3:
        st.metric(label='Minimum Price', value=df['Minimum Price']) 
