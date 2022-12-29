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

c1.image(Image.open('Images/near5-logo.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


  
