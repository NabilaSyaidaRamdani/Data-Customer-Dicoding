import streamlit as st

st.title("Welcome to My Streamlit App!")

st.header('HI! Our Dear Customer')

st.subheader('Please fill Your Name')

Name = st.text_input(label='Full Name', value='')

City = st.text_input(label='City', value='')

State = st.text_input(label='State', value='')

CustomerID = st.text_input(label='Customer ID', value='')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
    
import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/564x/ed/6b/be/ed6bbe5838979e5bca84c998cd2a87e6.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("customer.csv")
st.title("Visualisasi Top 10 Kota Berdasarkan Jumlah Pelanggan")
city_counts = df["customer_city"].value_counts().head(10)

fig, ax = plt.subplots()
ax.barh(city_counts.index, city_counts.values)
ax.set_xlabel("Number of Customers")
ax.set_title("Top 10 Cities by Number of Customers")

for index, value in enumerate(city_counts.values):
    ax.text(value, index, str(value))

# Menampilkan plot di Streamlit
st.pyplot(fig)
