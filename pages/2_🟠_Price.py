# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NEAR Price - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🟠 NEAR Price')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/near4-logo.JPG'))

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
    return None

NEAR_Price_per_Day = get_data('NEAR Price per Day')
Range_of_Price_Changes = get_data('Range of Price Changes')
NEAR_Price = get_data('NEAR Price')

# NEAR Price Analysis

df = NEAR_Price_per_Day
        
fig = px.area(df, x='Date', y='Price', color='CRITERIA', title='NEAR Price per Day (🟢Max 🔴Avg 🔵Min)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='$USD')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.LINE(df, x='Date', y='Price', color='CRITERIA', title='NEAR Price per Day', log_y=False, barmode='group')
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
