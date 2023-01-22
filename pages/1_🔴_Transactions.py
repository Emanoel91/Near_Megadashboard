# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Transactions - Near Megadashboard', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🔴 Transactions')

# Cover
c1 , c2 = st.columns(2)

c1.image(Image.open('Images/transactions.JPG'))

with c2: 
        st.subheader('📄 ***List of contents***')
        st.write(
                    """
                    1️⃣ **Overview**
             
                    2️⃣ **Daily Transactions**
            
                    3️⃣ **Activity of Addresses**
            
                    4️⃣ **Transaction Fees**
                    """
                  )

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
    elif query1 == 'Total/Average Transactions Fee':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9c150e27-bdf1-440c-bc44-244d2a7851b5/data/latest')
    elif query1 == 'Top 20 TX Signers Based on Paid Fees':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7f93109f-26e2-4472-b1b7-933920522958/data/latest')
    elif query1 == 'Statistical Data: Daily Transaction Fees':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8ee9bda4-fdbb-4e85-a2fb-1b472131d536/data/latest')
    elif query1 == 'Classification of Blocks Based on TX Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b72f2b79-46fc-40db-8a64-1738ad8a2ada/data/latest')
    elif query1 == 'Block Maximum Transaction Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d1b7ffcf-4b80-42cc-9d39-4978b8fb032a/data/latest')
    elif query1 == 'Distribution of Transactions Between Blocks':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ab4ef9d7-5dac-44c9-9c4c-401a73e5b087/data/latest')
    elif query1 == 'Classification of Transactions Based on TX Signers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/951de34b-673e-47dd-a85f-0e1b65bd5569/data/latest')
    elif query1 == 'Number of New Addresses':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ef7b7b14-4bff-4ce7-a39d-a719d90f6726/data/latest')
    elif query1 == 'Transactions Hitmap: Day of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d97d664d-92e3-41ef-9791-025c8fc6ee79/data/latest')
    elif query1 == 'Total Transactions Count Over Days of Week':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/446128c4-fd51-413a-9a5a-c7712dedc5e2/data/latest')
    elif query1 == 'Total Transactions Count Over Hours of Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3d42455d-a0e6-40e6-81b7-bc27ce1a6661/data/latest')
    elif query1 == 'Monthly Transactions Count of Top TX Signers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e8a73aa1-98cc-4575-9815-ce37d26dbe6f/data/latest')
    elif query1 == 'Monthly Transactions Count of Top TX Receivers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e77292ca-6973-4ace-a7a9-313057508618/data/latest')
    elif query1 == 'Monthly Transaction Fees of Top TX Signers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f9474172-0568-4605-a0f6-571ed3b20b9c/data/latest')
    elif query1 == 'Time interval between the first and last transaction':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5ebca19e-d680-4cd7-8fcf-6958ab206e09/data/latest')
    elif query1 == 'Distribution of the number of activity days':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/974f933f-18f2-4e70-bf3e-0c9320776524/data/latest')
    elif query1 == 'Max/Avg/Median/Min Transaction Fees':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f571f0fc-9187-402e-85e0-f4b73dd52ac3/data/latest')
    return None

transactions_overview = get_data('Transactions Overview')
Daily_Transactions_Data = get_data('Daily Transactions Data')
Status_of_Transactions = get_data('Status of Transactions')
Statistical_Data_Number_of_Transactions = get_data('Statistical Data: Number of Transactions')
Top_20_TX_Signers_Base_on_Transactions_Count = get_data('Top 20 TX Signers Base on Transactions Count')
Top_20_TX_Receivers_Base_on_Transactions_Count = get_data('Top 20 TX Receivers Base on Transactions Count')
Transaction_Fees = get_data('Transaction Fees')
Total_Average_Transactions_Fee = get_data('Total/Average Transactions Fee')
Top_20_TX_Signers_Based_on_Paid_Fees = get_data('Top 20 TX Signers Based on Paid Fees')
Statistical_Data_Daily_Transaction_Fees = get_data('Statistical Data: Daily Transaction Fees')
Classification_of_Blocks_Based_on_TX_Count = get_data('Classification of Blocks Based on TX Count')
Block_with_Maximum_Transaction_Count = get_data ('Block Maximum Transaction Count')
Distribution_of_Transactions_Between_Blocks = get_data('Distribution of Transactions Between Blocks')
Classification_of_Transactions_Based_on_TX_Signers = get_data('Classification of Transactions Based on TX Signers')
Number_of_New_Addresses = get_data('Number of New Addresses')
Transactions_Hitmap_Day_of_Week = get_data('Transactions Hitmap: Day of Week')
Total_Transactions_Count_Over_Days_of_Week = get_data('Total Transactions Count Over Days of Week')
Total_Transactions_Count_Over_Hours_of_Day = get_data('Total Transactions Count Over Hours of Day')
Monthly_Transactions_Count_of_Top_TX_Signers = get_data('Monthly Transactions Count of Top TX Signers')
Monthly_Transactions_Count_of_Top_TX_Receivers = get_data('Monthly Transactions Count of Top TX Receivers')
Monthly_Transaction_Fees_of_Top_TX_Signers = get_data('Monthly Transaction Fees of Top TX Signers')
Time_interval_between_the_first_and_last_transaction = get_data('Time interval between the first and last transaction')
Distribution_of_the_number_of_activity_days = get_data('Distribution of the number of activity days')
Max_Avg_Median_Min_Transaction_Fees = get_data('Max/Avg/Median/Min Transaction Fees')

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

fig = px.bar(df, x='Date', y='Transactions Count', color='Status', title='Status of Transactions (🔴Fail 🔵Success)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Status', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)

with c1:
   fig = go.Figure()
   for i in df['Status'].unique():
       fig.add_trace(go.Scatter(
           name=i,
           x=df.query("Status == @i")['Date'],
           y=df.query("Status == @i")['Transactions Count'],
           mode='lines',
           stackgroup='one',
           groupnorm='percent'
        ))
   fig.update_layout(title='Status of Transactions(%Normalized)')
   st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:         
   fig = px.pie(df, values='Transactions Count', names='Status', title='Total Transactions Count')
   fig.update_layout(legend_title='Status', legend_y=0.5)
   fig.update_traces(textinfo='percent+label', textposition='inside')
   st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Statistical_Data_Number_of_Transactions
c1, c2, c3, c4 = st.columns(4)
    
with c1:
        fig = px.bar(df, x='Status', y='Maximum', color='Maximum', title='📈 Maximum TX Count in a Day')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
        fig = px.bar(df, x='Status', y='Average', color='Average', title='📊 Average # of daily TXs')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c3:
        fig = px.bar(df, x='Status', y='Median', color='Median', title='📊 Median # of daily TXs')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c4:
        fig = px.bar(df, x='Status', y='Minimum', color='Minimum', title='📉 Minimum TX Count in a Day')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ------------------------------------------------------------------------------------------------------------------------------------------
df = Transactions_Hitmap_Day_of_Week
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TXs Count', histfunc='avg', title='Transactions Heat map: Day of Week', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TXs Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Transactions_Hitmap_Day_of_Week)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Total_Transactions_Count_Over_Days_of_Week
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='Day Name', y='Total TXs Count', color='Day Name', title='Total Transactions Count Over Days of Week', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Day Name', yaxis_title='Number of TXs', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Total_Transactions_Count_Over_Hours_of_Day        
with c2:
        fig = px.bar(df, x='Hour', y='Total TXs Count', color='Total TXs Count', title='Total Transactions Count Over Hours of Day', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Hour', yaxis_title='Number of TXs', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ------------------------------------------------------------------------------------------------------------------------------------------

df = Daily_Transactions_Data

fig = px.area(df, x='Date', y='Blocks Count', title='Daily Blocks Count')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Blocks Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Block_with_Maximum_Transaction_Count
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Block ID with the Max TX Count', value=df['Block ID'])
with c2:
        st.metric(label='Max TXs Count in a Block', value=df['Tx Count'])        

df = Classification_of_Blocks_Based_on_TX_Count
c1, c2 = st.columns(2)

with c1:
       fig = px.pie(df, values='Block Count', names='Class', title='Classification of Blocks Based on TX Count')
       fig.update_layout(legend_title='Class', legend_y=0.5)
       fig.update_traces(textinfo='percent+label', textposition='inside')
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:    
       fig = px.bar(df, x='Class', y='Block Count', color='Class', title='', log_y=True)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Number of TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Distribution_of_Transactions_Between_Blocks
fig = px.scatter(df.sort_values(['TX Count', 'Block Count'], ascending=[True, True]), x='TX Count', y='Block Count', title='Distribution of Transactions Between Blocks', log_x=True)
fig.update_layout(legend_title=None, xaxis_title='Transactions Count', yaxis_title='Blocks Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Daily_Transactions_Data        
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

st.subheader('3️⃣ Activity of Addresses')
df = Daily_Transactions_Data
fig = px.area(df, x='Date', y='Tx Senders Count', title='Number of Active Addresses')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# ------------------------------------------------------------------------------------------------------------------------------------------------
df = Number_of_New_Addresses
fig = px.area(df, x='Date', y='New Address Count', title='Number of New Addresses')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ------------------------------------------------------------------------------------------------------------------------------------------------
df = Time_interval_between_the_first_and_last_transaction
fig = px.line(df.sort_values(['Difference', 'Total Address'], ascending=[True, True]), x='Difference', y='Total Address', title='Time interval between the first and last transaction', log_x=True, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Time interval', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Distribution_of_the_number_of_activity_days
fig = px.line(df.sort_values(['Days Active', 'Total Address'], ascending=[True, True]), x='Days Active', y='Total Address', title='Distribution of the number of activity days', log_x=True, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Days Count', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# ------------------------------------------------------------------------------------------------------------------------------------------------
df = Classification_of_Transactions_Based_on_TX_Signers
c1, c2 = st.columns(2)

with c1:
       fig = px.pie(df, values='TX Signers Count', names='Class', title='Classification of Transactions Based on TX Signers')
       fig.update_layout(legend_title='Class', legend_y=0.5)
       fig.update_traces(textinfo='percent+label', textposition='inside')
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:    
       fig = px.bar(df, x='Class', y='TX Signers Count', color='Class', title='', log_y=True)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='Number of TX Signers', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# -------------------------------------------------------------------------------------------------------------------------------------------------
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
# --------------------------------------------------------------------------------------------------------------------------------------------------
df = Monthly_Transactions_Count_of_Top_TX_Signers
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='Date', y='TXs Count', color='TX Signer', title='Monthly Transactions Count of Top TX Signers', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transaction', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Monthly_Transactions_Count_of_Top_TX_Receivers       
        
with c2:
        fig = px.bar(df, x='Date', y='TXs Count', color='TX Receiver', title='Monthly Transactions Count of Top TX Receivers', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Transaction')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# --------------------------------------------------------------------------------------------------------------------------------------------------        
st.subheader('4️⃣ Transaction Fees')
df = Transaction_Fees

fig = px.area(df, x='Date', y='Transactions Fee', title='Total Daily Transaction Fees')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Fee($NEAR)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Max_Avg_Median_Min_Transaction_Fees
fig = px.area(df, x='Date', y='Fee', color='Criteria', title='Max/Avg/Median/Min Transaction Fees', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='($NEAR)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Total_Average_Transactions_Fee
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Transactions Fee($NEAR)', value=df['Total Transactions Fee'])
                
with c2:
        st.metric(label='Averag Transactions Fee($NEAR)', value=df['Averag Transactions Fee'])
        
df = Top_20_TX_Signers_Based_on_Paid_Fees
c1, c2 = st.columns(2)
    
with c1:
        fig = px.bar(df, x='TX Signer', y='Transactions Fee', title='Top 20 TX Signers Based on Paid Fees')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Statistical_Data_Daily_Transaction_Fees        
with c2:
        fig = px.bar(df, x='CRITERIA', y='Fee', color='Fee', title='Statistical Data: Daily Transaction Fees')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$NEAR')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    

df = Monthly_Transaction_Fees_of_Top_TX_Signers
fig = px.bar(df, x='Date', y='TXs Fee', color='TX Signer', title='Monthly Transaction Fees of Top TX Signers', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Fee($NEAR)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
