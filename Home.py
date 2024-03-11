# import necessary packages
import streamlit as st
from PIL import Image
from dotenv import dotenv_values



# set page configurations
st.set_page_config(
    page_title= 'Home', layout= "wide",
    initial_sidebar_state= 'collapsed'
)
# retrieve user credentials
# retrieve database credentials into variables
cred = dotenv_values('.env')

# Extract individual values from cred dictionary
user = cred.get('USER')
name = cred.get('NAME')
password = cred.get('USER_PWD')

def entered_cred():
    if 'user' in st.session_state and 'pass' in st.session_state:
        entered_user = st.session_state['user'].strip()
        entered_pass = st.session_state['pass'].strip()

        if entered_user == user and entered_pass == password:
            st.success('Login successful!', icon="✅")
            st.session_state['authenticated'] = True
            
        else:
            st.session_state['authenticated'] = False
            if not entered_pass:
                st.warning('Please enter a password')
            elif not entered_user:
                st.warning('Please enter a username')
            else:
                st.error('Invalid username or PIN', icon="❌")

        print(f"authenticated: {st.session_state['authenticated']}")

def authenticate_user():
    if 'authenticated' not in st.session_state:
        st.subheader("Login")
        # username
        st.text_input(label="Username", placeholder='Your e-mail or username', max_chars=30, key='user', on_change=entered_cred)
        # password
        st.text_input(label="PIN", placeholder='Insert your 8-digit PIN', type="password", max_chars=8, key='pass', on_change=entered_cred)
        return False
    else:
        if st.session_state['authenticated']:
            return True
        else:
        # username
            st.text_input(label="Username", placeholder='Your e-mail or username', max_chars=30, key='user', on_change=entered_cred)
        # password
            st.text_input(label="PIN", placeholder='Insert your 8-digit PIN', type="password", max_chars=8, key='pass', on_change=entered_cred)
            return False


if authenticate_user():
    st.sidebar.button('Logout')

    col1, col2 = st.columns(spec=[1, 1], gap='medium')

    with col1:
        # Load App logo image
        icon = Image.open("no background.png")
        st.image(icon, width=400, channels='BGR')
        # App description
        st.title('**Welcome to** :violet[ChurnCo]👋👋')
        st.markdown('A data app that helps you track churning customers before they know it.')
        st.markdown('')
        st.markdown('')
        st.markdown("""    
            ChurnCo by Xenon®️ aims at understanding, analyzing, and ultimately reducing customer attrition within telecommunications
            services using machine learning models that will predict the likelihood of a customer churning.
        """)

    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("""### **Key Features:**
- Data: View external or in-built data on customer churning.
- Dashboard: Understand customer churn with visuals
- Predict: Predict the likelihood of a customer churning.
        """)

        st.markdown('### Live Demo:')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')

        st.markdown("""### User Perks:
- Better insight into customer preference
- Insight into churn triggers
- Early detection of potential churners
- Save investment.
        """)

    col3, col4, col5 = st.columns(3)
    with col3:
        # Add a GitHub button/link
        github_link = "[![GitHub](https://img.shields.io/badge/GitHub-Profile-brightgreen.svg)](https://github.com/elle-shika/Sunny-ChurnCo)"
        st.markdown(github_link, unsafe_allow_html=True)
    with col4:
        # Add a Gmail button/link
        gmail_link = "[![Gmail](https://img.shields.io/badge/Gmail-Send%20Email-red.svg)](mailto:pamelakushika@gmail.com)"
        st.markdown(gmail_link, unsafe_allow_html=True)
    with col5:
        # Add a LinkedIn button/link
        linkedin_link = "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue.svg)](https://www.linkedin.com/in/michelle_pamela/)"
        st.markdown(linkedin_link, unsafe_allow_html=True)
