# import necessary packages
import streamlit as st
from PIL import Image


# set page configurations
st.set_page_config(
    page_title= 'Home', layout= "centered",
    initial_sidebar_state= 'collapsed'
)

# load App logo image
icon = Image.open("no background.png")
st.image(icon, width= 400, channels= 'BGR')


# App description
st.title('**Welcome to** :violet[ChurnCo]')
st.markdown('A data app that helps you track churning customers before they know it.')


# User credentials
st.subheader("Login")
user = st.text_input( label= "Username", placeholder= ' Your e-mail or username',  max_chars= 30 )

#password
password = st.text_input(label= "PIN", placeholder= 'Insert your 8-digit PIN',  type= "password",  max_chars=8)

#submit credentials
st.button('Login')

# work on authentication

# login status
st.success('Login successful!', icon="✅")

st.error('Invalid username or PIN', icon= "❌")