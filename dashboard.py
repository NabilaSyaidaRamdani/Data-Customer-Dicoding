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


import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title("Visualisasi Top 10 Kota Berdasarkan Jumlah Pelanggan")

# Mengunggah file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca data dari file CSV
    df = pd.read_csv(uploaded_file)

    # Pastikan kolom 'customer_city' ada di dalam dataset
    if 'customer_city' in df.columns:
        # Menghitung 10 kota teratas berdasarkan jumlah pelanggan
        city_counts = df["customer_city"].value_counts().head(10)

        # Membuat visualisasi menggunakan Plotly
        fig = px.bar(city_counts, x=city_counts.values, y=city_counts.index, orientation='h', 
                     labels={'x': 'Number of Customers', 'y': 'Cities'}, title="Top 10 Cities by Number of Customers")

        # Menampilkan plot di Streamlit
        st.plotly_chart(fig)
    else:
        st.error("Kolom 'customer_city' tidak ditemukan di dalam dataset.")
else:
    st.write("Silakan unggah file CSV untuk melihat visualisasi.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", page_icon='🌏', layout='wide')
st.subheader("Customer Analysis")
st.markdown("##")

# Load the data
data = pd.read_csv("customer.csv")

# Sidebar image
st.sidebar.image("download.jpeg", caption="Customer Monitoring")

# Filter for states
st.sidebar.header("Please Filter Here")
state = st.sidebar.multiselect(
    "Customer State",
    options=data["customer_state"].unique(),
    default=data["customer_state"].unique()
)

# Filter data based on selected states
df_selection = data[data["customer_state"].isin(state)]

# --- Top 10 States by Number of Customers ---
st.subheader("Top 10 States by Number of Customers")

# Calculate top 10 states by customer count
state_counts = df_selection["customer_state"].value_counts().head(10)

# Plotting Scatter Plot using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(state_counts.values, state_counts.index, color='blue', s=100, alpha=0.7)

# Customizing the plot
ax.set_xlabel("Number of Customers", fontsize=12)
ax.set_ylabel("State", fontsize=12)
ax.set_title("Top 10 States by Number of Customers", fontsize=16, fontweight='bold')

# Adding data labels to the points
for index, value in enumerate(state_counts.values):
    ax.text(value, index, str(value), va='center', fontsize=10)

# Display plot in Streamlit
st.pyplot(fig)

