# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NFTs - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🟤 NFTs')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/nft2.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'NFT Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/12bc5e06-fc32-4096-81f4-a326f776f7f3/data/latest')
    elif query1 == 'NFT Daily':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/23787a50-b7ad-47e4-8721-da89580d31f7/data/latest')
    elif query1 == 'Distribution of NFT Purchases Among Different Price':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5b755517-4597-4a15-bf46-bd07a535684f/data/latest') 
    elif query1 == 'Distribution of Sellers By Number of Sold NFTs':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0eba6155-fd68-4a39-b916-d43c05928729/data/latest')
    elif query1 == 'Distribution of Buyers By Number of Purchased NFTs':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/851ad6a0-f495-4020-9f07-0cc16ce10bf3/data/latest')
    elif query1 == 'marketplace':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/42d2ede7-28b2-4345-a3b4-fd6cc00045f9/data/latest')
    elif query1 == 'Collections':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/661c9e2f-fcbc-40f3-8582-4e5185f7cdbc/data/latest')
    elif query1 == 'NFTs':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3fd9a5bb-7884-439a-a31b-f3a8e2dbdc86/data/latest')
    elif query1 == 'Top 20 NFT Sellers By Sales':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fd3e38d7-2cbb-4944-85f1-f70d9ba53727/data/latest')
    elif query1 == 'Top 20 NFT Sellers By Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c0a16020-ab70-4e60-ba42-0ca5de424217/data/latest')
    elif query1 == 'Top 20 NFT Buyers By Purchases':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5ec4e594-6b6a-4cf3-bdd7-3120c6eaf96f/data/latest')
    elif query1 == 'Top 20 NFT Buyers By Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e903d543-b4fa-43d1-8a51-b9081031d1e3/data/latest')
    return None    
    
NFT_Overview = get_data('NFT Overview')
NFT_Daily = get_data('NFT Daily')    
Distribution_of_NFT_Purchases_Among_Different_Price = get_data('Distribution of NFT Purchases Among Different Price')
Distribution_of_Sellers_By_Number_of_Sold_NFTs = get_data('Distribution of Sellers By Number of Sold NFTs')
Distribution_of_Buyers_By_Number_of_Purchased_NFTs = get_data('Distribution of Buyers By Number of Purchased NFTs')
marketplace = get_data('marketplace')    
Collections = get_data('Collections')
NFTs = get_data('NFTs')
Top_20_NFT_Sellers_By_Sales = get_data('Top 20 NFT Sellers By Sales')
Top_20_NFT_Sellers_By_Volume = get_data('Top 20 NFT Sellers By Volume')    
Top_20_NFT_Buyers_By_Purchases = get_data('Top 20 NFT Buyers By Purchases')
Top_20_NFT_Buyers_By_Volume = get_data('Top 20 NFT Buyers By Volume')

# NFT Analysis
st.subheader('1️⃣ Overview')
df = NFT_Overview
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='Total NFT Sales Volume($USD)', value=df['Total Volume'])
        st.metric(label='Total Number of NFT Sales', value=df['Total Purchases'].round(2))
        st.metric(label='Total Number of Purchased (Known) NFT Collections', value=df['Total Collections'].round(3))
with c2:
        st.metric(label='Total Number of Sellers', value=df['Total Sellers'])
        st.metric(label='NFT Sales Average Price($USD)', value=df['Average Price'].round(2))
        st.metric(label='Total Number of (Known) Marketplaces', value=df['Total Marketplace'].round(3))
with c3:
        st.metric(label='Total Number of Buyers', value=df['Total Buyers'])
        st.metric(label='Total Number of Purchased NFTs', value=df['Total NFTs'].round(2))
        
st.subheader('2️⃣ Daily Observations')
df = NFT_Daily
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='DATE', y='VOLUME', title='NFT Purchases Volume Over Time', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Line(x=df['DATE'], y=df['BUYER'], name='Buyers Count'), secondary_y=False)
        fig.add_trace(go.Line(x=df['DATE'], y=df['SELLERS'], name='Sellers Count'), secondary_y=True)
        fig.update_layout(title_text='Unique NFT Sellers & Buyers Over Time')
        fig.update_yaxes(title_text='', secondary_y=False)
        fig.update_yaxes(title_text='', secondary_y=True)
        st.plotly_chart(fig, use_container_width=False, theme=theme_plotly)
        
with c2:
        fig = px.bar(df, x='DATE', y='PURCHASES', title='Number of NFT Purchases Over Time', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        

    
