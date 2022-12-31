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

c1.image(Image.open('Images/transfer.JPG'))

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

st.subheader('1️⃣ Transfers Overview')
df = Statistical_Data_Transfers
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Transfers Volume($NEAR)', value=df['Transfers Volume'])
        st.metric(label='Unique Receivers Count', value=df['Receivers Count'].round(2))

with c2:
        st.metric(label='Total Transfers Count', value=df['Transfers Count'])
        st.metric(label='Unique Senders Count', value=df['Senders Count'].round(2))
        
st.subheader('2️⃣ Daily Transfers')
df = Transfers

fig = px.bar(df, x='Date', y='Transfers Volume', color='STATUS', title='Daily Transfers Volume', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='STATUS', yaxis_title='$NEAR', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)









