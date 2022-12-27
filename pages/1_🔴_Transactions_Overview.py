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
    if query1 == 'Transactions Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5954ddc8-9cdf-47cc-b4cb-a67a0d05f75b/data/latest')
    elif query1 == 'Daily Transactions Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/28aad408-cba3-4560-9235-7a5026a5cd1b/data/latest')
        
    return None

transactions_overview = get_data('Transactions Overview')
Daily_Transactions_Data = get_data('Daily Transactions Data')

# chain Analysis
st.subheader('Overview')
df = transactions_overview
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Transactions Count', value=df['Total Transactions Count'])
        st.metric(label='Successful Transactions', value=df['Successful Transactions'].round(2))
        st.metric(label='Total Blocks Count', value=df['Total Blocks Count'].round(3))
        st.metric(label='Total Tx Senders Count', value=df['Total Tx Senders Count'].round(4))
        st.metric(label='Average Transactions Count per Sender', value=df['Average Transactions Count per Sender'].round(5))
with c2:
        st.metric(label='Average Success Rate', value=df['Average Success Rate'])
        st.metric(label='Failed Transactions', value=df['Failed Transactions'].round(2))
        st.metric(label='Average Transaction Count per Block', value=df['Average Transaction Count per Block'].round(3))
        st.metric(label='Total Tx Receivers Count', value=df['Total Tx Receivers Count'].round(4))
        st.metric(label='Average Transactions Count per Receiver', value=df['Average Transactions Count per Receiver'].round(5))
        
st.subheader('Daily Transactions Analysis')
df = Daily_Transactions_Data

fig = px.area(df, x='DAY', y='Transactions Count', title='Daily Transactions Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transactions Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)













    
