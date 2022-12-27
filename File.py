# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Dashboard Name', page_icon=':bar_chart:', layout='wide')
st.title('Dashboard Name')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/flipsidecrypto-logo.png'))
c2.image(Image.open('Images/near-logo.png'))
c3.image(Image.open('Images/metricsdao-logo.png'))

st.write("")
st.write("")
st.write("")
st.write("")

st.write(
    """
comments
    """
)

st.subheader('Purposes of Dashboard')
st.write(
    """
comments
    """
)

st.subheader('Methodology')
st.write(
    """
comments
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Developer/Analyst: [@Astiran91](https://twitter.com/Astiran91)**', icon="📌")
with c2:
    st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
with c3:
    st.info('**Data: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")

