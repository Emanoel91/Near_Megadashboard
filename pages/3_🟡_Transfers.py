# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Transfers - Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('🟡 Transfers')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/transfer2.JPG'))

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query3):
    if query3 == 'Transfers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2c3c92a7-a763-42e0-b902-81c41d1c364e/data/latest')
    elif query3 == 'Statistical Data: Transfers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4439d22a-ac32-41cd-a9ca-2fcccea4be20/data/latest')
    elif query3 == 'Top 20 Senders based on Sending Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c63dcc08-0732-4d52-a8d5-6138d71bd9e9/data/latest') 
    elif query3 == 'Top 20 Senders Based on Sending Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fbdbccd7-ef3a-46d4-b6c8-b0a44d71a3e9/data/latest')
    elif query3 == 'Top 20 Receivers based on Receiving Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6548465f-eade-493b-bf8a-63d4f8fe08e3/data/latest')
    elif query3 == 'Top 20 Receivers based on Receiving Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8c4c6a35-dacf-4d7c-a63f-a27f17a31e0b/data/latest')
    elif query3 == 'Classification of Transfers Based on Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/98f12856-04e8-470e-98ad-6793b71766da/data/latest')
    elif query3 == 'Classification of Senders Based on Sending Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b56338db-194a-4399-ab91-2ef4e7f14e08/data/latest')
    elif query3 == 'Classification of Receivers Based on Receiving Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0f7931af-1972-4eeb-a650-c43f13a9407d/data/latest')
    elif query3 == 'Transfers Status':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0f5ed59e-1c80-4c76-9aeb-80dcd98a1e87/data/latest')
    elif query3 == 'Sending Volume of Top Senders per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9766d23e-c03a-420b-9ef3-d4f4715fb8c0/data/latest')
    elif query3 == 'Receiving Volume of Top Receivers per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3a02bbeb-a037-456d-935f-b1aebcc9b82a/data/latest')
    elif query3 == 'Sending Count of Top Senders per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/30a2c8e0-b588-4003-9141-cbb66895216d/data/latest')
    elif query3 == 'Receiving Count of Top Receivers per Month':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8cda0b43-0826-4599-80be-0ab26dbfb447/data/latest')
    elif query3 == 'Share of Users':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/59485509-0f80-434f-a649-6f6606cdb888/data/latest')
    elif query3 == 'Number of Unique Senders & Receivers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2aeba64e-1462-47ba-bcb3-600bba69cc65/data/latest')
    elif query3 == 'Transfers Hitmap: Day of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/475ce9c1-aa07-4a27-b8ad-b19cd9b877fb/data/latest')
    elif query3 == 'Total Transfers Volume Over Days of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d80b7582-d6fb-40e8-b5dd-aa54b9e70e69/data/latest')
    elif query3 == 'Total Transfers Volume Over Hours of Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/de752500-973a-4a07-9247-aa6106d2e77f/data/latest')
    return None

Transfers = get_data('Transfers')
Statistical_Data_Transfers = get_data('Statistical Data: Transfers')
Top_20_Senders_based_on_Sending_Volume = get_data('Top 20 Senders based on Sending Volume')
Top_20_Senders_Based_on_Sending_Count = get_data('Top 20 Senders Based on Sending Count')
Top_20_Receivers_based_on_Receiving_Volume = get_data('Top 20 Receivers based on Receiving Volume')
Top_20_Receivers_based_on_Receiving_Count = get_data('Top 20 Receivers based on Receiving Count')
Classification_of_Transfers_Based_on_Volume = get_data('Classification of Transfers Based on Volume')
Classification_of_Senders_Based_on_Sending_Volume = get_data('Classification of Senders Based on Sending Volume')
Classification_of_Receivers_Based_on_Receiving_Volume = get_data('Classification of Receivers Based on Receiving Volume')
Transfers_Status = get_data('Transfers Status')
Sending_Volume_of_Top_Senders_per_Month = get_data('Sending Volume of Top Senders per Month')
Receiving_Volume_of_Top_Receivers_per_Month = get_data('Receiving Volume of Top Receivers per Month')
Sending_Count_of_Top_Senders_per_Month = get_data('Sending Count of Top Senders per Month')
Receiving_Count_of_Top_Receivers_per_Month = get_data('Receiving Count of Top Receivers per Month')
Share_of_Users = get_data('Share of Users')
Number_of_Unique_Senders_Receivers = get_data('Number of Unique Senders & Receivers')
Transfers_Hitmap_Day_of_Week = get_data('Transfers Hitmap: Day of Week')
Total_Transfers_Volume_Over_Days_of_Week = get_data('Total Transfers Volume Over Days of Week')
Total_Transfers_Volume_Over_Hours_of_Day = get_data('Total Transfers Volume Over Hours of Day')

st.subheader('1️⃣ Transfers Overview')
df = Statistical_Data_Transfers
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Transfers Volume($NEAR)', value=df['Transfers Volume'])
        st.metric(label='Unique Receivers Count', value=df['Receivers Count'].round(2))

with c2:
        st.metric(label='Total Transfers Count', value=df['Transfers Count'])
        st.metric(label='Unique Signers Count', value=df['Senders Count'].round(2))
        
st.subheader('2️⃣ Daily Transfers')
df = Transfers

fig = px.bar(df, x='Date', y='Transfers Volume', color='STATUS', title='Daily Transfers Volume(🔴Failed 🔵Successful)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='STATUS', yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='Date', y='Transfers Count', color='STATUS', title='Daily Transfers Count(🔴Failed 🔵Successful)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='STATUS', yaxis_title='', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
c1, c2, c3 = st.columns(3)
    
with c1:
        fig = px.pie(df, values='Transfers Count', names='STATUS', title='Share of Transfers Count')
        fig.update_layout(legend_title='Status', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
df = Transfers_Status
with c2:
        fig = px.bar(df, x='Status', y='Transfers Count', color='Transfers Count', title='Total Transfers Count', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transfers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c3:        
        fig = px.bar(df, x='Status', y='Volume', color='Volume', title='Total Transfers Volume', log_y=True)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# --------------------------------------------------------------------------------------------------------------------------------
c1, c2 = st.columns(2)
df = Number_of_Unique_Senders_Receivers
with c1:
        fig = px.bar(df, x='Date', y='User Count', color='User Type', title='Number of Unique Signers & Receivers')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Address Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Share_of_Users        
with c2:
        fig = px.pie(df, values='User Count', names='User Type', title='Share of Users')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Transfers_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='Transfers Volume', histfunc='avg', title='Transfers Hitmap Day of Week', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='Transfers Volume'))
fig.update_yaxes(categoryorder='array', categoryarray=Transfers_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
st.subheader('3️⃣ Top Addresses')
df = Top_20_Senders_based_on_Sending_Volume
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='Sender', y='Sending Volume', color='Sending Volume', title='Top 20 Senders based on Sending Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Top_20_Receivers_based_on_Receiving_Volume
with c2:
        fig = px.bar(df, x='Receiver', y='Receiving Volume', color='Receiving Volume', title='Top 20 Receivers based on Receiving Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ------------------------------------------------------------------------------------------------------------------------------------------------        
df = Sending_Volume_of_Top_Senders_per_Month
fig = px.bar(df, x='Date', y='Volume', color='Sender Address', title='Sending Volume of Top Senders per Month', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Receiving_Volume_of_Top_Receivers_per_Month
fig = px.bar(df, x='Date', y='Volume', color='Receiver Address', title='Receiving Volume of Top Receivers per Month', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        
# -------------------------------------------------------------------------------------------------------------------------------------------------        
        
df = Top_20_Senders_Based_on_Sending_Count
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='Sender', y='Sending Count', color='Sending Count', title='Top 20 Senders Based on Sending Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Top_20_Receivers_based_on_Receiving_Count
with c2:
        fig = px.bar(df, x='Receiver', y='Receiving Count', color='Receiving Count', title='Top 20 Receivers based on Receiving Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
df = Sending_Count_of_Top_Senders_per_Month
fig = px.bar(df, x='Date', y='Sending Count', color='Sender Address', title='Sending Count of Top Senders per Month', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sending Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Receiving_Count_of_Top_Receivers_per_Month
fig = px.bar(df, x='Date', y='Receiving Count', color='Receiver Address', title='Receiving Count of Top Receivers per Month', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Receiving Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# -----------------------------------------------------------------------------------------------------------------------------------------------------        

st.subheader('4️⃣ Classifications')        
df = Classification_of_Transfers_Based_on_Volume
c1, c2, c3 = st.columns(3)
    
with c1:
        fig = px.pie(df, values='Tx Count', names='CLASS', title='Classification of Transfers Based on Volume')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='CLASS', y='Tx Count', color='CLASS', title='', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Transactions', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Senders_Based_on_Sending_Volume
with c2:
        fig = px.pie(df, values='Senders Count', names='CLASS', title='Classification of Senders Based on Sending Volume')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='CLASS', y='Senders Count', color='CLASS', title='', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Senders', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Classification_of_Receivers_Based_on_Receiving_Volume
with c3:
        fig = px.pie(df, values='Receivers Count', names='CLASS', title='Classification of Receivers Based on Receiving Volume')
        fig.update_layout(legend_title='CLASS', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='CLASS', y='Receivers Count', color='CLASS', title='', log_y=True)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='CLASS', yaxis_title='Number of Receivers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)




