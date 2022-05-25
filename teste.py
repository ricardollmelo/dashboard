from bcb import sgs
import streamlit as st
import pandas as pd
import pyIpeaData as ipea
import seaborn as sb
##### Definindo os títulos #####
st.header('Dashboard Macroeconômico')
st.markdown(
    '*Os principais indicadores macroeconômicos - IPCA; PIB; BALANÇA COMERCIAL, INPC, DESEMPREGO.*')
###### Importando dados ######
selic = sgs.get({'selic': 432}, start='2010-01-01')
st.title('SELIC')
st.line_chart(selic)
st.title('IPCA')
ipca = sgs.get({'IPCA': 433}, start='2010-01-01')
st.line_chart(ipca)
st.title('Taxa de desemprego (%)')
desem = sgs.get({'Taxa de desemprego (%)': 24369}, start='2012-03-01')
st.line_chart(desem)
