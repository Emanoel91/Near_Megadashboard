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
    return None

NEAR_Price_per_Day = get_data('NEAR Price per Day')

# NEAR Price Analysis

df = NEAR_Price_per_Day
        
fig = px.area(df, x='Date', y='Price', color='CRITERIA', title='NEAR Price per Day', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Price:🟢Max 🔴Avg 🔵Min')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

  
