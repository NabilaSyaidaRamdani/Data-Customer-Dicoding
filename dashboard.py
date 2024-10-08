import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Dashboard",page_icon='✨',layout='wide')
st.subheader("Customer Here!!")
st.markdown("##")

# Membaca data
data = pd.read_csv("customer.csv")

st.sidebar.image("",caption="Analisis Data Customer")

st.markdown(
    """
    <style>
    .css-1d391kg {
        background-color: #0083B8; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

