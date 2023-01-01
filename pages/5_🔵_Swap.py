# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Swap - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🔵 Swap')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/swap2.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Swap Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4dcac99e-fc75-4106-9c95-4365ff45485c/data/latest')
    elif query1 == 'Daily Swaps':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6f485435-f301-4138-8efc-91bac8b57143/data/latest')
    elif query1 == 'Classification of Swaps Based on Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ec6dcf38-a6e4-4c24-9690-6ba7133d71b3/data/latest') 
    elif query1 == 'Classification of Swappers Total Swap Size':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8a8e7ee2-ec3b-4469-8b7a-82101f76e1f9/data/latest')
    elif query1 == 'Classification of Swappers Average Swap Size':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0467f64c-aac5-468c-9966-8687ebb7a37c/data/latest')
    elif query1 == 'Swap Type':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2ffc1972-04fe-4465-823f-83c65b3ca291/data/latest')
    elif query1 == 'Near DEXs':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/17afcd87-c684-4201-ae2d-ecaacad35a29/data/latest')
    elif query1 == 'Token in':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9d5e4d09-a51e-4189-aaf8-188de1ca7dac/data/latest')
    elif query1 == 'Token out':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fe3fd77d-227a-451b-ac39-7b5fd8061dca/data/latest')
    elif query1 == 'Swaps Hitmap: Day of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/76e4ef3f-4cdf-4750-a5b7-7cdb109181aa/data/latest')
    elif query1 == 'Swaps Hitmap: Hour of Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/82bce493-8d9d-433e-afbd-6093cc4be799/data/latest')
    elif query1 == 'Tokens':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e1a2e763-dfe2-467a-81a1-b30a43d6666f/data/latest')
    return None

Swap_Overview = get_data('Swap Overview')
Daily_Swaps = get_data('Daily Swaps')
Classification_of_Swaps_Based_on_Volume = get_data('Classification of Swaps Based on Volume')
Classification_of_Swappers_Total_Swap_Size = get_data('Classification of Swappers Total Swap Size')
Classification_of_Swappers_Average_Swap_Size = get_data('Classification of Swappers Average Swap Size')
Swap_Type = get_data('Swap Type')
Near_DEXs = get_data('Near DEXs')
Token_in = get_data('Token in')
Token_out = get_data('Token out')
Swaps_Hitmap_Day_of_Week = get_data('Swaps Hitmap: Day of Week')    
Swaps_Hitmap_Hour_of_Day = get_data('Swaps Hitmap: Hour of Day') 
Tokens = get_data('Tokens')

# Swap Analysis
st.subheader('1️⃣ Overview')
df = Swap_Overview
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='Swaps Volume($USD)', value=df['Swaps Volume'])
        st.metric(label='Average Swap Volume($USD)', value=df['Average Swap Volume'].round(2))
with c2:
        st.metric(label='Swaps Count', value=df['Swaps Count'])
        st.metric(label='Number of Token In', value=df['Number of Token In'].round(2))
with c3:
        st.metric(label='Swappers Count', value=df['Swappers Count'])
        st.metric(label='Number of Token Out', value=df['Number of Token Out'].round(2))
        
st.subheader('2️⃣ Daily Swaps')
df = Daily_Swaps

c1, c2 = st.columns(2)

with c1:
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Swaps Volume'], name='Total Volume'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Average Swaps Volume'], name='Average Volume'), secondary_y=True)
        fig.update_layout(title_text='Swaps Volume Over Time')
        fig.update_yaxes(title_text='$USD', secondary_y=False)
        fig.update_yaxes(title_text='$USD', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:         
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df['Date'], y=df['Swaps Count'], name='Swaps'), secondary_y=False)
        fig.add_trace(go.Line(x=df['Date'], y=df['Swappers Count'], name='Swappers'), secondary_y=True)
        fig.update_layout(title_text='Number of Swaps & Swappers')
        fig.update_yaxes(title_text='', secondary_y=False)
        fig.update_yaxes(title_text='', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        
st.subheader('3️⃣ Classifications')

c1, c2, c3 = st.columns(3)
df = Classification_of_Swaps_Based_on_Volume

with c1:
        fig = px.pie(df, values='SWAPS', names='CLASS', title='Classification of Swaps Based on Volume')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Swappers_Total_Swap_Size        
with c2:  
        fig = px.pie(df, values='Swappers Count', names='CLASS', title='Classification of Swappers Total Swap Size')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Classification_of_Swappers_Average_Swap_Size    
with c3:
        fig = px.pie(df, values='Swappers Count', names='CLASS', title='Classification of Swappers Average Swap Size')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
c1, c2, c3 = st.columns(3)
df = Classification_of_Swaps_Based_on_Volume

with c1:      
        fig = px.bar(df, x='CLASS', y='SWAPS', color='CLASS', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Swappers_Total_Swap_Size        
with c2:  
        fig = px.bar(df, x='CLASS', y='Swappers Count', color='CLASS', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Classification_of_Swappers_Average_Swap_Size    
with c3: 
        fig = px.bar(df, x='CLASS', y='Swappers Count', color='CLASS', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
st.subheader('4️⃣ Stablecoin Swaps')
c1, c2, c3, c4 = st.columns(4)
df = Swap_Type

with c1:      
        fig = px.bar(df, x='Swap Type', y='Swaps Volume', color='Swap Type', title='Total Volume of Swaps By Type', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Swap Type', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
               
with c2:  
        fig = px.bar(df, x='Swap Type', y='Average Swap Volume', color='Swap Type', title='Average Swap Volume By Type', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Swap Type', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c3: 
        fig = px.bar(df, x='Swap Type', y='Swaps Count', color='Swap Type', title='Total Number of Swaps By Type', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Swap Type', yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c4: 
        fig = px.bar(df, x='Swap Type', y='Swappers Count', color='Swap Type', title='Total Number of Swappers By Type', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Swap Type', yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        

st.subheader('5️⃣ Near DEXs')        
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/ref_finance.png'))    
c2.image(Image.open('Images/jumbo.png'))  

c1 , c2, c3, c4 = st.columns(4)
df = Near_DEXs

with c1:      
        fig = px.bar(df, x='DEX', y='Swaps Volume', color='DEX', title='Total Volume of Swaps By DEX', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='DEX', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
               
with c2:  
        fig = px.bar(df, x='DEX', y='Average Swap Volume', color='DEX', title='Average Swap Volume By DEX', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='DEX', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c3: 
        fig = px.bar(df, x='DEX', y='Swaps Count', color='DEX', title='Total Number of Swaps By DEX', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='DEX', yaxis_title='Swaps', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c4: 
        fig = px.bar(df, x='DEX', y='Swappers Count', color='DEX', title='Total Number of Swappers By DEX', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='DEX', yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  

st.subheader('6️⃣ Token in vs. Token out') 
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/swap3.JPG'))    

df = Tokens
fig = px.bar(df, x='Token', y='Buying Volume', color='Buying Volume', title='Total Buying Volume By Token', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Token', yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 



              
