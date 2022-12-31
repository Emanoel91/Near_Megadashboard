# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Transactions - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🔴 Transactions')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/chain1-logo.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Transactions Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5954ddc8-9cdf-47cc-b4cb-a67a0d05f75b/data/latest')
    elif query1 == 'Daily Transactions Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/28aad408-cba3-4560-9235-7a5026a5cd1b/data/latest')
    elif query1 == 'Status of Transactions':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/accec9ec-512b-4a63-9170-80b37e53e242/data/latest') 
    elif query1 == 'Statistical Data: Number of Transactions':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e31e9f16-3294-4104-8514-bc071c400c0d/data/latest')
    elif query1 == 'Top 20 TX Signers Base on Transactions Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/99663018-9ec2-4e00-a827-3078fcaa7761/data/latest')
    elif query1 == 'Top 20 TX Receivers Base on Transactions Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a6ff61aa-4d96-4c53-912f-9c922e7926e7/data/latest')
    elif query1 == 'Transaction Fees':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b688e249-b644-4040-8059-d8c7cea2d258/data/latest')
    return None

transactions_overview = get_data('Transactions Overview')
Daily_Transactions_Data = get_data('Daily Transactions Data')
Status_of_Transactions = get_data('Status of Transactions')
Statistical_Data_Number_of_Transactions = get_data('Statistical Data: Number of Transactions')
Top_20_TX_Signers_Base_on_Transactions_Count = get_data('Top 20 TX Signers Base on Transactions Count')
Top_20_TX_Receivers_Base_on_Transactions_Count = get_data('Top 20 TX Receivers Base on Transactions Count')
Transaction_Fees = get_data('Transaction Fees')

# NEAR Analysis
st.subheader('1️⃣ Overview')
df = transactions_overview
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Transactions Count', value=df['Total Transactions Count'])
        st.metric(label='Successful Transactions', value=df['Successful Transactions'].round(2))
        st.metric(label='Total Blocks Count', value=df['Total Blocks Count'].round(3))
        st.metric(label='Total Tx Signers Count', value=df['Total Tx Senders Count'].round(4))
        st.metric(label='Average Transactions Count per Signer', value=df['Average Transactions Count per Sender'].round(5))
with c2:
        st.metric(label='Average Success Rate', value=df['Average Success Rate'])
        st.metric(label='Failed Transactions', value=df['Failed Transactions'].round(2))
        st.metric(label='Average Transaction Count per Block', value=df['Average Transaction Count per Block'].round(3))
        st.metric(label='Total Tx Receivers Count', value=df['Total Tx Receivers Count'].round(4))
        st.metric(label='Average Transactions Count per Receiver', value=df['Average Transactions Count per Receiver'].round(5))
        
st.subheader('2️⃣ Daily Transactions')
df = Status_of_Transactions

fig = px.bar(df, x='Date', y='Transactions Count', color='Status', title='Status of Transactions', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig.update_layout(title='Status of Transactions(%Normalized)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
fig = go.Figure()
for i in options:
    fig.add_trace(go.Scatter(
        name=i,
        x=df.query("Status == @i")['Date'],
        y=df.query("Status == @i")['Transactions Count'],
        mode='lines',
        stackgroup='one',
        groupnorm='percent'
     ))

df = Statistical_Data_Number_of_Transactions
c1, c2, c3, c4 = st.columns(4)
    
with c1:
        fig = px.bar(df, x='Status', y='Maximum', title='Maximum TX Count in a Day')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
        fig = px.bar(df, x='Status', y='Average', title='Average # of daily TXs')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c3:
        fig = px.bar(df, x='Status', y='Median', title='Median # of daily TXs')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c4:
        fig = px.bar(df, x='Status', y='Minimum', title='Minimum TX Count in a Day')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


df = Daily_Transactions_Data

fig = px.area(df, x='Date', y='Transactions Count', title='Daily Transactions Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.area(df, x='Date', y='Blocks Count', title='Daily Blocks Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Blocks Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.line(df, x='Date', y='Average Transaction Count per Block', title='Average Transaction Count per Block', log_y=True)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='TX per Block', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Average Transactions Count per Sender'], name='TX per Sender'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Average Transactions Count per Receiver'], name='TX per Receiver'), secondary_y=True)
fig.update_layout(title_text='Average Transactions Count per User')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Tx Senders Count'], name='TX Senders Count'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Tx Receivers Count'], name='TX Receivers Count'), secondary_y=True)
fig.update_layout(title_text='Number of Transaction Senders/Receivers')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Top_20_TX_Signers_Base_on_Transactions_Count
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='TX Signer', y='TXs Count', color='TXs Count', title='Top 20 TX Signers Base on Transactions Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Top_20_TX_Receivers_Base_on_Transactions_Count       
        
with c2:
        fig = px.bar(df, x='TX Receiver', y='TXs Count', color='TXs Count', title='Top 20 TX Receivers Base on Transactions Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
st.subheader('3️⃣ Transaction Fees')
df = Transaction_Fees

fig = px.area(df, x='Date', y='Transactions Fee', title='Daily Transaction Fees')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Fee($NEAR)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

  
