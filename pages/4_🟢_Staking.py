# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Staking - Near Megadashboard', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🟢 Staking')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/staking2.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Daily Staking/unstaking':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/388c8081-dfad-4668-a850-a4a74303bcd0/data/latest')
    elif query1 == 'Staking Overview':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c4b604b9-66ae-4023-8eb3-27b14202648e/data/latest')
    elif query1 == 'Top 20 Pools Based on Staked Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/32b688dd-c247-47a1-bd03-676be82cde41/data/latest') 
    elif query1 == 'Staked Volume in Top Pools Over Time':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/364a97a5-a160-4650-81ab-172c757fdcb3/data/latest')
    elif query1 == 'Top 20 Pools Based on Staking Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e6ca73e8-a686-45c1-a31b-0a1125d866db/data/latest')
    elif query1 == 'Staking Count in Top Pools Over Time':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/160f31d8-2b59-4b2a-97fd-bde2f90bd284/data/latest')
    elif query1 == 'Classification of Staking Based on Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cfc15aa3-8bb3-4a4a-89bc-fdbe2fe101df/data/latest')
    elif query1 == 'Classification of Stakers Total Staking Size':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/296b278c-2c99-4510-8ef0-957e18cd1892/data/latest')
    elif query1 == 'Classification of Stakers Average Staking Size':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6067262b-f79d-4897-9e56-2e7cb7332411/data/latest')
    elif query1 == 'Staking Hitmap: Day of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/23644ba5-d8ef-4ebf-abd8-457f13acf759/data/latest')
    elif query1 == 'Staking on each Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3d409bba-0f8d-423e-86f1-5c65a6bd50b5/data/latest')
    elif query1 == 'Staking on each Hour':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b36465bb-beed-4415-b511-7b9c119af672/data/latest')
    elif query1 == 'Unstaking Hitmap: Day of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7e1e89ac-1c78-4bd0-9981-0e5356f3fd42/data/latest')
    elif query1 == 'Unstaking on each Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e6ecb418-b15c-47b3-ba85-29eabcb9a3c8/data/latest')  
    elif query1 == 'Unstaking on each Hour':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c7c753cf-1ca3-494c-a38e-73fd125f47d1/data/latest')
    return None  

Daily_Staking_unstaking = get_data('Daily Staking/unstaking')
Staking_Overview = get_data('Staking Overview')
Top_20_Pools_Based_on_Staked_Volume = get_data('Top 20 Pools Based on Staked Volume')
Staked_Volume_in_Top_Pools_Over_Time = get_data('Staked Volume in Top Pools Over Time')
Top_20_Pools_Based_on_Staking_Count = get_data('Top 20 Pools Based on Staking Count')
Staking_Count_in_Top_Pools_Over_Time = get_data('Staking Count in Top Pools Over Time')
Classification_of_Staking_Based_on_Volume = get_data('Classification of Staking Based on Volume')
Classification_of_Stakers_Total_Staking_Size = get_data('Classification of Stakers Total Staking Size')
Classification_of_Stakers_Average_Staking_Size = get_data('Classification of Stakers Average Staking Size')
Staking_Hitmap_Day_of_Week = get_data('Staking Hitmap: Day of Week')    
Staking_on_each_Day = get_data('Staking on each Day') 
Staking_on_each_Hour = get_data('Staking on each Hour')
Unstaking_Hitmap_Day_of_Week = get_data('Unstaking Hitmap: Day of Week')
Unstaking_on_each_Day = get_data('Unstaking on each Day')
Unstaking_on_each_Hour = get_data('Unstaking on each Hour')

# Staking Analysis
st.subheader('1️⃣ Overview')
df = Staking_Overview
c1, c2, c3 = st.columns(3)

with c1:      
        fig = px.bar(df, x='Action', y='Total Volume', color='Action', title='Total Volume of Actions', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
               
with c2:  
        fig = px.bar(df, x='Action', y='Action Count', color='Action', title='Total Number of Actions', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='Transaction', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
with c3: 
        fig = px.bar(df, x='Action', y='Total Users', color='Action', title='Total Number of Users', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Action', yaxis_title='User', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
    
st.subheader('2️⃣ Daily Staking & Unstaking')
df = Daily_Staking_unstaking 

# Volume of Actions ------------------------------------------------------------------------------------------------------------------

fig = px.bar(df.sort_values(['Date', 'Action Volume'], ascending=[True, False]), x='Date', y='Action Volume', color='Action', title='Daily Actions Volume')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume($NEAR)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = go.Figure()
for i in df['Action'].unique():
    fig.add_trace(go.Scatter(
        name=i,
        x=df.query("Action == @i")['Date'],
        y=df.query("Action == @i")['Action Volume'],
        mode='lines',
        stackgroup='one',
        groupnorm='percent'
     ))
fig.update_layout(title='Daily Share of Actions Volume (%Normalized)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Staking & Unstaking Count --------------------------------------------------------------------------------

fig = px.bar(df.sort_values(['Date', 'Action Count'], ascending=[True, False]), x='Date', y='Action Count', color='Action', title='Daily Actions Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = go.Figure()
for i in df['Action'].unique():
    fig.add_trace(go.Scatter(
        name=i,
        x=df.query("Action == @i")['Date'],
        y=df.query("Action == @i")['Action Count'],
        mode='lines',
        stackgroup='one',
        groupnorm='percent'
     ))
fig.update_layout(title='Daily Share of Actions Count (%Normalized)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
     
# Stakers ----------------------------------------------------------------------------------------------------

fig = px.bar(df.sort_values(['Date', 'Users Count'], ascending=[True, False]), x='Date', y='Users Count', color='Action', title='Daily Users Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='User')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = go.Figure()
for i in df['Action'].unique():
    fig.add_trace(go.Scatter(
        name=i,
        x=df.query("Action == @i")['Date'],
        y=df.query("Action == @i")['Users Count'],
        mode='lines',
        stackgroup='one',
        groupnorm='percent'
     ))
fig.update_layout(title='Daily Share of Users Count (%Normalized)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
st.subheader('3️⃣ Top Pools')
# Volume ----------------------------------------------------------------------------------------------------------------------------------
df = Top_20_Pools_Based_on_Staked_Volume
c1, c2 = st.columns(2)

with c1:      
        fig = px.bar(df, x='Pool', y='Volume', color='Action', title='Top 20 Pools Based on Staked Volume', log_y=True, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume($NEAR)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
df = Staked_Volume_in_Top_Pools_Over_Time        
with c2:
        fig = px.bar(df.sort_values(['Date', 'Volume'], ascending=[True, False]), x='Date', y='Volume', color='Pool', title='Staked Volume in Top Pools per Month')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Volume($NEAR)')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
# Pool Overview Based on Number of Staking ----------------------------------------------------------------------------------------------------        
df = Top_20_Pools_Based_on_Staking_Count
c1, c2 = st.columns(2)

with c1:      
        fig = px.bar(df, x='Pool', y='Action Count', color='Action', title='Top 20 Pools Based on Staking Count', log_y=True, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transaction', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
df = Staking_Count_in_Top_Pools_Over_Time       
with c2:
        fig = px.bar(df.sort_values(['Date', 'Staking Count'], ascending=[True, False]), x='Date', y='Staking Count', color='Pool', title='Staking Count in Top Pools per Month')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transaction')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
        
st.subheader('4️⃣ Classifications')

c1, c2, c3 = st.columns(3)
df = Classification_of_Staking_Based_on_Volume

with c1:
        fig = px.pie(df, values='Staking Count', names='Class', title='Classification of Transactions Based on Staked Volume')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Stakers_Total_Staking_Size        
with c2:  
        fig = px.pie(df, values='Stakers Count', names='Class', title='Classification of Stakers Total Staking Size')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Classification_of_Stakers_Average_Staking_Size     
with c3:
        fig = px.pie(df, values='Stakers Count', names='Class', title='Classification of Stakers Average Staking Size')
        fig.update_layout(legend_title='Class', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
c1, c2, c3 = st.columns(3)
df = Classification_of_Staking_Based_on_Volume

with c1:      
        fig = px.bar(df, x='Class', y='Staking Count', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Number of Stakes', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Stakers_Total_Staking_Size        
with c2:  
        fig = px.bar(df, x='Class', y='Stakers Count', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Number of Stakers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Classification_of_Stakers_Average_Staking_Size    
with c3: 
        fig = px.bar(df, x='Class', y='Stakers Count', color='Class', title='', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Number of Stakers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        
        
st.subheader('5️⃣ Staking & Unstaking Pattern')
df = Staking_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='Staking Volume', histfunc='avg', title='Staking Volume Hitmap, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Volume($NEAR)'))
fig.update_yaxes(categoryorder='array', categoryarray=Staking_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Unstaking_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='Unstaking Volume', histfunc='avg', title='Unstaking Volume Hitmap, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Volume($NEAR)'))
fig.update_yaxes(categoryorder='array', categoryarray=Unstaking_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
df = Staking_on_each_Day

with c1:      
        fig = px.bar(df, x='Day Name', y='Total Staking Volume', color='Day Name', title='Total Staked Volume on each Day', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Day Name', yaxis_title='Volume ($NEAR)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = Staking_on_each_Hour        
        
        fig = px.bar(df, x='Hour', y='Total Staking Volume', color='Total Staking Volume', title='Total Staked Volume on each Hour', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Volume', yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Unstaking_on_each_Day        
with c2:  
        fig = px.bar(df, x='Day Name', y='Total Unstaking Volume', color='Day Name', title='Total Unstaked Volume on each Day', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Day Name', yaxis_title='Volume($NEAR)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        df = Unstaking_on_each_Hour
        fig = px.bar(df, x='Hour', y='Total Unstaking Volume', color='Total Unstaking Volume', title='Total Unstaked Volume on each Hour', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Volume', yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
# ----------------------------------------------------------------------------------------------------------------------

df = Staking_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='Staking Count', histfunc='avg', title='Staking Count Hitmap, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Staking Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Staking_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Unstaking_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='Unstaking Count', histfunc='avg', title='Unstaking Count Hitmap, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Unstaking Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Unstaking_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
df = Staking_on_each_Day

with c1:      
        fig = px.bar(df, x='Day Name', y='Total Staking Count', color='Day Name', title='Total Staking Count on each Day', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Day Name', yaxis_title='Stakes', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        df = Staking_on_each_Hour        
        
        fig = px.bar(df, x='Hour', y='Total Staking Count', color='Total Staking Count', title='Total Staking Count on each Hour', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Stakes', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Unstaking_on_each_Day        
with c2:  
        fig = px.bar(df, x='Day Name', y='Total Unstaking Count', color='Day Name', title='Total Unstaking Count on each Day', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Day Name', yaxis_title='Unstakes', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        df = Unstaking_on_each_Hour
        fig = px.bar(df, x='Hour', y='Total Unstaking Count', color='Total Unstaking Count', title='Total Unstaking Count on each Hour', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Unstakes', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        
        
        
        
        
        
        
    
