# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Layout
st.set_page_config(page_title='Transactions Overview - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🔴 Transactions Overview')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Trnsactions Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5954ddc8-9cdf-47cc-b4cb-a67a0d05f75b/data/latest')
        
    return None

transactions_overview = get_data('Trnsactions Overview')

# Single chain Analysis
st.subheader('Overview')
df = transactions_overview
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Blocks Count', value=df['Total Blocks Count'])
        st.metric(label='Total Transactions Count', value=df['Total Transactions Count'].round(2))
        st.metric(label='Total Transactions Count per Receiver', value=df['Total Transactions Count per Receiver'].round(3))
with c2:
        st.metric(label='Total Tx Receivers Count', value=df['Total Tx Receivers Count'])
        st.metric(label='Total Tx Senders Count', value=df['Total Tx Senders Count'].round(2))
        st.metric(label='Total Transactions Count per Sender', value=df['Total Transactions Count per Sender'].round(3))
    
