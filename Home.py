# Descriptions:
# Help Metrics DAO create the ultimate collection of on-chain analytics, data, and insights with our new Megadashboards challenge! These are serious challenges that 
# require plenty of work — and offer increased payouts in return. Read on for more info:
# We’re putting together the ultimate analytics tool for the NEAR ecosystem, a dazzling dashboard full of glittering insights — and we need your help!
# Create a dashboard that offers a holistic view of the NEAR ecosystem, including activity, supply, staking, and development. Your dashboard should focus on providing 
# everything a newcomer or experienced user should know, organized and presented in a way that is simple to understand, easy to navigate, and understandable and 
#valuable for novices and experienced users alike.


# 📚 Libraries
import streamlit as st
from PIL import Image


# Title
st.set_page_config(page_title='Near Megadashboard', page_icon=':chart_with_upwards_trend:', layout='wide')
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

5️⃣ The NEAR protocol does not follow Polkadot, BSC, or Solana networks that use 64-character public keys; Rather, by abandoning the use of public keys for wallets, 
the wallets of this network are the first wallets in which people's addresses are the same as their profile names. Therefore, the Near network not only aims to make 
the process of developing and creating various programs easy for developers, but also users can easily benefit from its services.
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
In this dashboard, an overview of the Near ecosystem from various aspects is displayed for users. In this dashboard, users can monitor the status of Near network 
transactions. Follow the price status of the native coin of this network i.e. NEAR and the stable coin of this chain i.e. USN. On the other hand, they can check 
transfers between different addresses. Staking is when users lock crypto assets for a set period of time to help support the operation of a blockchain. In this 
dashboard, the status of staking in the Near network can also be seen by users. Swapping refers to exchanging one coin or token for another. If users want to know the 
status of swaps in various DEXs on the Near network, they can refer to the "Swap" page in this dashboard. Finally, since NFTs are one of the most popular topics in the
crypto world, all information about this fascinating topic is accessible to users on the "NFTs" page.
    """
)

st.subheader('📖 Guidance')
st.write(
    """
- Most of the charts are displayed on the daily time frame. Only the charts related to the activity of the top users are displayed in the monthly time frame.
- The charts that show the volume index are some in terms of 'USD' and others in terms of 'NEAR'. (Note the labels on the charts.)
    """
)

st.write(
    """
###### 🤝 thanks to:
- [Mo_Defi](https://twitter.com/Mo_Defi) and [pinehearst](https://twitter.com/pinehearst_) for using some of their queries. ([Flipside World Cup: Crosschain Defi Monitoring](https://app.flipsidecrypto.com/dashboard/flipside-world-cup-crosschain-defi-monitoring-dxlso0) & [The City of NEAR](https://app.flipsidecrypto.com/dashboard/xG8L9i))
- [Ali Taslimi](https://twitter.com/AliTslm) for getting ideas from his awesome dashboard [Cross Chain Monitoring Tool](https://cross-chain-monitoring.streamlit.app/)
    """
)
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    c3.image(Image.open('Images/metricsdao.JPG'))






