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
The main goal of the NEAR network is to create an infrastructure for creating a new Internet. In the new internet, it will be harder for big companies to access 
people's personal information. Countries cannot ban some programs and destroy people's business in this system. A world of freedom where everyone can act freely. 
Of course, this goal of the Near network is not a new concept; In fact, Satoshi Nakamoto also pursued the same goal by introducing Bitcoin in 2008. But Bitcoin has 
created this freedom only in the financial sphere. But like many other networks, Near seeks to expand this freedom to other aspects of human life.
###### 👌 Near protocol features
1️⃣ The speed of transactions in Near network is high and the transaction fees are low. The reason for this is that Near protocol uses sharding technology.

2️⃣ Scalability is an important concept in the blockchain world. Near protocol uses sharding technology to solve the scalability problem. In this model, a transaction 
does not need to be checked by all network nodes. With sharding, a network is transformed into several parallel networks that check transactions simultaneously, so t
hat each transaction is checked in a shard. As a result, only nodes present in a shard will check and confirm this transaction, and other nodes present in other 
shards of the network will not check this transaction. This idea makes the capacity of the network increase significantly.

3️⃣ Sharding technology is also used by other protocols and for this reason Near protocol is not the first network. In many networks that use sharding, relatively 
complex hardware equipment is needed to set up a node; Therefore, fewer people are able to set up nodes in these networks; But the Near protocol uses the cloud space 
of the host to launch the node.

4️⃣ Unlike other layer 1 networks such as Avalanche, which adopted Solidity to make it easier to integrate with Ethereum, NEAR became a developer-first network with support 
for WebAssembly (WASM).
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






