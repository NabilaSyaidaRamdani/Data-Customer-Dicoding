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


# Membuat tombol Sign In
if st.button('Sign In'):
    # Membuka tab baru menggunakan JavaScript
    js = """
    <script type="text/javascript">
        window.open('https://your-sign-in-url.com', '_blank').focus();
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)


# Membuat tombol Sign In
if st.button('Sign UP'):
    # Membuka tab baru menggunakan JavaScript
    js = """
    <script type="text/javascript">
        window.open('https://your-sign-in-url.com', '_blank').focus();
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)
 
st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
import streamlit as st

# Define the pages
pages = ["Page 1 - Cat", "Page 2 - Dog", "Page 3 - Owl"]

# Add a selectbox for navigation
page = st.selectbox("Select a page:", pages)

# Display content based on the selected page
if page == "Page 1 - Cat":
    st.header("Page 1: Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    
elif page == "Page 2 - Dog":
    st.header("Page 2: Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    
elif page == "Page 3 - Owl":
    st.header("Page 3: Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
