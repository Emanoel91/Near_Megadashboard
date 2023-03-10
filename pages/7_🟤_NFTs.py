# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NFTs - Near Megadashboard', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🟤 NFTs')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/nft5.JPG'))
with c2: 
        st.subheader('📄 ***List of contents***')
        st.write(
                    """
                    1️⃣ **Overview**
             
                    2️⃣ **Daily Observations**
                    
                    3️⃣ **Classifications**
                    
                    4️⃣ **NFT Marketplace**
                                
                    """
                )

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
    elif query1 == 'Number of Sellers & Buyers in each Marketplaces ':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a702da0a-ac29-43f1-9c64-19135cfd9cd4/data/latest')
    elif query1 == 'Top 20 NFTs By Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a4a35a6f-2857-4c1d-bf5f-99b62771ca04/data/latest')
    return None    
    
NFT_Overview = get_data('NFT Overview')
NFT_Daily = get_data('NFT Daily')    
Distribution_of_NFT_Purchases_Among_Different_Price = get_data('Distribution of NFT Purchases Among Different Price')
Distribution_of_Sellers_By_Number_of_Sold_NFTs = get_data('Distribution of Sellers By Number of Sold NFTs')
Distribution_of_Buyers_By_Number_of_Purchased_NFTs = get_data('Distribution of Buyers By Number of Purchased NFTs')
marketplace = get_data('marketplace')    
Collections = get_data('Collections')
NFTs = get_data('NFTs')
Top_20_NFTs_By_Volume = get_data('Top 20 NFTs By Volume')
Top_20_NFT_Sellers_By_Sales = get_data('Top 20 NFT Sellers By Sales')
Top_20_NFT_Sellers_By_Volume = get_data('Top 20 NFT Sellers By Volume')    
Top_20_NFT_Buyers_By_Purchases = get_data('Top 20 NFT Buyers By Purchases')
Top_20_NFT_Buyers_By_Volume = get_data('Top 20 NFT Buyers By Volume')
Number_of_Sellers_Buyers_in_each_Marketplaces = get_data('Number of Sellers & Buyers in each Marketplaces ')

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
        
with c2:
        fig = px.bar(df, x='DATE', y='PURCHASES', title='Number of NFT Purchases Over Time', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        
         
df = NFT_Daily
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df['DATE'], y=df['BUYER'], name='Buyers Count'), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df['SELLERS'], name='Sellers Count'), secondary_y=True)
fig.update_layout(title_text='Unique NFT Sellers & Buyers Over Time')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=False, theme=theme_plotly)

df = NFT_Daily
fig = px.bar(df, x='DATE', y='Average Price', title='NFT Purchases Average Price Over Time', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        
        
st.subheader('3️⃣ Classifications')
df = Distribution_of_NFT_Purchases_Among_Different_Price 
c1, c2, c3 = st.columns(3)
    
with c1:
        fig = px.pie(df, values='PURCHASES', names='Class', title='Classification of NFT Purchases Among Different Price')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
        
        fig = px.bar(df, x='Class', y='PURCHASES', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Purchases Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
# -------------------------------------------------------------------------------------------------------------------------------------------------------
df = Distribution_of_NFT_Purchases_Among_Different_Price
with c2:
        fig = px.pie(df, values='SELLERS', names='Class', title='Classification of Sellers Among Different Price')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)     
        
        fig = px.bar(df, x='Class', y='SELLERS', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Sellers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------
df = Distribution_of_NFT_Purchases_Among_Different_Price
with c3:        
        fig = px.pie(df, values='BUYERS', names='Class', title='Classification of Buyers Among Different Price')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Class', y='BUYERS', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Buyers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------        

df = Distribution_of_Sellers_By_Number_of_Sold_NFTs 
c1, c2 = st.columns(2)
    
with c1:
        fig = px.pie(df, values='SELLERS', names='Sales Count', title='Distribution of Sellers By Number of Sold NFTs')
        fig.update_layout(legend_title='Sales Count', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Sales Count', y='SELLERS', color='Sales Count', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Sales Count', yaxis_title='Sellers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Distribution_of_Buyers_By_Number_of_Purchased_NFTs    
with c2:    
        fig = px.pie(df, values='BUYERS', names='Purchases Count', title='Distribution of Buyers By Number of Purchased NFTs')
        fig.update_layout(legend_title='Purchases Count', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Purchases Count', y='BUYERS', color='Purchases Count', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Purchases Count', yaxis_title='Buyers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
st.subheader('4️⃣ NFT Marketplaces')
df = marketplace

# Cover
c1 , c2, c3 = st.columns(3)

c1.image(Image.open('Images/paras.JPG'))
c2.image(Image.open('Images/apollo42.JPG'))
c3.image(Image.open('Images/uniqart.JPG'))
 
c1, c2 = st.columns(2)
    
with c1:
        fig = px.pie(df, values='Purchases', names='Marketplace', title='Distribution of NFT Purchases Among Marketplaces')
        fig.update_layout(legend_title='Marketplace', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Marketplace', y='Purchases', color='Marketplace', title='', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Marketplace', yaxis_title='Purchases Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Marketplace', y='Average Price', color='Average Price', title='Marketplaces Average NFT Purchase Price', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Marketplace', yaxis_title='Price($USD)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c2:    
        fig = px.pie(df, values='Volume', names='Marketplace', title='Distribution of NFT Purchases Volume($USD) Among Marketplaces')
        fig.update_layout(legend_title='Marketplace', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Marketplace', y='Volume', color='Marketplace', title='', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Marketplace', yaxis_title='Volume($USD)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = Number_of_Sellers_Buyers_in_each_Marketplaces
        fig = px.bar(df, x='Marketplace', y='Users Count', color='User Type', title='Number of Sellers & Buyers in each Marketplaces', log_y=True, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Address', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        
df = Collections
fig = px.scatter(df.sort_values(['VOLUME', 'PURCHASES'], ascending=[True, True]), x='VOLUME', y='PURCHASES', color='COLLECTION_NAME', title='💎Top 100 Collections Purchases vs. Volume', log_x=True, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Purchases Volume($USD)', yaxis_title='Purchases Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.scatter(df.sort_values(['SELLERS', 'BUYERS'], ascending=[True, True]), x='SELLERS', y='BUYERS', color='COLLECTION_NAME', title='🎴Top 100 Collections Sellers vs. Buyers')
fig.update_layout(legend_title=None, xaxis_title='Sellers Count', yaxis_title='Buyers Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df.sort_values(['COLLECTION_NAME', 'AVG_PRICE'], ascending=[True, True]), x='COLLECTION_NAME', y='AVG_PRICE', color='COLLECTION_NAME', title='🧿Top 100 Collections Average Price')
fig.update_layout(legend_title=None, xaxis_title='', yaxis_title='Average Price($USD)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
c1, c2 = st.columns(2)
    
df = NFTs
with c1:
        fig = px.bar(df, x='NFT_NAME', y='PURCHASES', color='PURCHASES', title='Top 20 NFTs Based on Purchases Count', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='NFT_NAME', yaxis_title='Purchases Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
        
        df = Top_20_NFT_Sellers_By_Sales
        fig = px.bar(df, x='SELLER', y='SALES', color='SALES', title='Top 20 NFT Sellers Based on Sales Count', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='SELLER', yaxis_title='Sales Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = Top_20_NFT_Buyers_By_Purchases
        fig = px.bar(df, x='BUYER', y='PURCHASES', color='PURCHASES', title='Top 20 NFT Buyers Based on Purchases Count', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='BUYER', yaxis_title='Purchases Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Top_20_NFTs_By_Volume
with c2:
        fig = px.bar(df, x='NFT_NAME', y='VOLUME', color='VOLUME', title='Top 20 NFTs Based on Purchases Volume', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='NFT_NAME', yaxis_title='Volume($USD)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
        
        df = Top_20_NFT_Sellers_By_Volume
        fig = px.bar(df, x='SELLER', y='VOLUME', color='VOLUME', title='Top 20 NFT Sellers Based on Sales Volume', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='SELLER', yaxis_title='Sales Volume($USD)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = Top_20_NFT_Buyers_By_Volume
        fig = px.bar(df, x='BUYER', y='VOLUME', color='VOLUME', title='Top 20 NFT Buyers Based on Purchases Volume', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='BUYER', yaxis_title='Purchases Volume($USD)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


    
