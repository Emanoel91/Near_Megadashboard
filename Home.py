# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Near Megadashboard', page_icon=':bar_chart:', layout='wide')
st.title('Near Ⓜegadashboard')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/near2-logo.png'))

st.subheader('📃 Introduction')


st.write(
    """
Today, if someone wants to use a simple application or game launched on the blockchain platform, he has to go through many steps; Therefore, the Near network has 
put its main focus on the usability and user-friendliness of its platform; Developers and programmers and end users of products launched on the Near platform should 
feel better and more comfortable when using it. This network is very similar to Ethereum in terms of idea and is a platform for launching decentralized applications.
The Near protocol is similar to the Ethereum network; With the difference that this chain tries to provide higher usability, scalability, and ease, and finally be a completely decentralized network.
The NEAR protocol provides a platform where programmers can freely present their programs. With such programs, we will have a better world where people are fully in control of their assets, be it money, personal 
information, etc.
###### 🤔 What is the purpose of creating the Near protocol?

    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
comments
    """
)

st.subheader('🧠 Methodology')
st.write(
    """
comments
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [@Astiran91](https://twitter.com/Astiran91)**', icon="📌")
    c1.image(Image.open('Images/analyst.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    c3.image(Image.open('Images/metricsdao.JPG'))






