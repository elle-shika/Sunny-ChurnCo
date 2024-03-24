# import necessary packages
import streamlit as st
import pandas as pd
import pyodbc as pc
from dotenv import dotenv_values
import openpyxl
import time

# set page configurations
st.set_page_config(
    page_title= 'Data', layout ='wide'
)

# Connection to SQL databases
# retrieve database credentials into variables
cred = dotenv_values('.env')

# extract individual values from cred dictionary
db = cred.get('DATABASE')
host = cred.get('SERVER')
user = cred.get('USERNAME')
password = cred.get('PASSWORD')

# build connection_string
connection_string = f"DRIVER={{SQL Server}};SERVER={host};DATABASE={db};UID={user};PWD={password}"

# build connection
nection = pc.connect(connection_string)

def detail():        
    col1, col2, col3 = st.columns([1,2,2])
    with col1:
        st.subheader('🎯Info:')
        st.markdown('- Dataset contains data on demographics, subscriptions and financial details of customers of a Telco.')
        st.markdown('- Dataset structured into **12 columns**.')
        st.markdown('- **3** numerical columns')            
        st.markdown('- **5** boolean features')              
        st.markdown('- **13** object features')
    with col2:
        st.markdown('''### 📚📖Dictionary:
- **Gender** - Specifies the sex of the customer
- **SeniorCitizen** - Specifies if the customer is a senior citizen or not
- **Partner** - Specifies whether the customer has a partner or not
- **Dependents** - Specifies whether the customer has dependents or not
- **Tenure** -  Duration of subscription in months
- **Phone Service** - if the customer has a phone service or not
- **MultipleLines** - If the customer has multiple lines or not
- **InternetService** - Customer's internet service provider 
- **OnlineSecurity** - If the customer has online security or not
- **OnlineBackup** - If the customer has online backup or not.''') 

    with col3:
        st.subheader('')
        st.subheader('')
        st.markdown('''
- **DeviceProtection** - If the customer has device protection or not
- **TechSupport** - If the customer has tech support or not
- **StreamingTV** - Whether the customer has streaming TV or not
- **StreamingMovies** - Whether the customer has streaming movies or not
- **Contract** - The contract term of the customer
- **PaperlessBilling** - Whether the customer has paperless billing or not
- **Payment Method** - The customer's payment method
- **MonthlyCharges** - Monthly charges to the customer 
- **TotalCharges** - Total amount charged to the customer
- **Churn** - Whether the customer churned or not. ''')



def get_data():
    # Function to get data from varying sources and display data IN DISPLAY DATA SECTION ON APP PAGE
    with st.form('Data entry Display'):
        st.subheader('Get Data')  # Row title
        selection = st.selectbox(label='Select churn data source', options=['In-built data', 'External data'], key='source_selection')  # data source options
        choice = st.form_submit_button('Select')

    if choice and selection == 'In-built data':
        # display internal data
        # write sql queries
        query1 = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
        # load data
        customer_df = pd.read_sql_query(query1, nection)
        with st.spinner("Dataset loading..."):
            time.sleep(3)
        st.subheader('View Data')
        st.write(customer_df.head(20))

    else:
        if selection == 'External data':
            file_upload = st.file_uploader(label = 'Choose a CSV file', type= 'csv', key = 'external data')
            if file_upload is not None:
                customer_df2 = pd.read_csv(file_upload)
                with st.spinner("Dataset loading..."):
                    time.sleep(3)
                st.subheader('View Data')
                st.dataframe(customer_df2.head(20))
        

if __name__ == "__main__":
    st.title('Customer Churn Data')
    get_data()
    detail()