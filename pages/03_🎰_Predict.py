# import necessary packages
import streamlit as st
import time
import joblib
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, RobustScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.pipeline import Pipeline as impipeline
from Transformer import LogTransformer, FeatureSelector


# set page configurations
st.set_page_config(
    page_title= "Let's Predict",
    layout = 'wide'
)
st.title('Customer Churn Prediction')


# load prediction models
st.cache_resource() #cache churn prediction models
def load_tools():
    global log_reg, sgd_model, encoder
    log_reg = joblib.load('.\model\Churn_Predictor.joblib') #load  logistic regression model
    sgd_model = joblib.load('.\model\Churn_SGD_Predictor.joblib') # load SGD model
    encoder = joblib.load('.\model\Encoder.joblib') # load encoder
    return log_reg, sgd_model, encoder


def model_pick():
    column1, column2 = st.columns(2)
    with column1:
        # function allowing user to select a prediction model
        st.selectbox(label= '**Select your predictor.**', options =['Logistic Regression', 'SGD'], key = 'predictor_choice')

    with column2:
        # insert an animation or image
        pass


def input_save():
    # function to save all user input as a test dataframe
        # retrieve inputs from session state
    keys = [gender,senior_citizen ,partner , dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv,
               streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges]
    gender = st.session_state['gender']
    senior_citizen = st.session_state['senior_citizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = st.session_state['tenure']
    phone_service = st.session_state['phone_service']
    multiple_lines = st.session_state['multiple_lines']
    internet_service = st.session_state['internet_service']
    online_security = st.session_state['online_security']
    online_backup = st.session_state['online_backup']
    device_protection = st.session_state['device_protection']
    tech_support = st.session_state['tech_support']
    streaming_tv = st.session_state['streaming_tv']
    streaming_movies = st.session_state['streaming_movies']
    contract = st.session_state['contract']
    paperless_billing = st.session_state['paperless_billing']
    payment_method = st.session_state['payment_method']
    monthly_charges = st.session_state['monthly_charges']
    total_charges = st.session_state['total_charges']


    # store inputs as list
    inputs = [[gender,senior_citizen ,partner , dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv,
               streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges]]

    # Create Dataframe of inputs
    test_df = pd.DataFrame(inputs,columns=['Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'Tenure', 'PhoneService','MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
                        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'])
#     #Define global variables
#     global test_df 
#     test_df = []  # Initialize test_df
#     if submit:
    return test_df  


def feature_inputs():
    # Function to collect features inputs from user
    st.write('**Enter description of Customer you want to assess.**') 
 
    
    with st.form('Customer_information'):
        column1, column2, column3, column4, column5 = st.columns(5)
        with column1:
            st.write('##### **Personal Details**')
            gender = st.selectbox('Gender:', options=['Male', 'Female'], key = 'gender')
            senior_citizen = st.selectbox('SeniorCitizen:', options=['Yes', 'No'], key = 'senior_citizen')
            partner = st.selectbox('Partner:', options=['Yes', 'No'], key = 'partner')
            dependents = st.selectbox('Dependents:', options=['Yes', 'No'], key = 'dependents')
            
 
        with column2:
            st.write('##### **Products And Services**')
            phone_service = st.selectbox('PhoneService:', options=['Yes', 'No'], key = 'phone_service')
            multiple_lines = st.selectbox('MultipleLines:', options=['Yes', 'No', 'No phone service'], key = 'multiple_lines')
            internet_service = st.selectbox('InternetService:', options=['DSL', 'Fiber Optic', 'No internet service'], key ='internet_service')
            device_protection = st.selectbox('DeviceProtection:', options=['Yes', 'No', 'No internet service'], key = 'device_protection')
            tech_support = st.selectbox('TechSupport:', options=['Yes', 'No', 'No internet service'], key = 'tech_support')
           
 
        with column3:
            st.write('##### **Online Services**')
            online_security = st.selectbox('OnlineSecurity:', options=['Yes', 'No', 'No internet service'], key = 'online_security')
            online_backup = st.selectbox('OnlineBackup:', options=['Yes', 'No', 'No internet service'], key = 'online_backup')
            streaming_tv = st.selectbox('StreamingTv:', options=['Yes', 'No', 'No internet service'], key = 'streaming_tv')
            streaming_movies = st.selectbox('StreamingMovies:', options=['Yes', 'No', 'No internet service'], key = 'streaming_movies')
 
        with column4:
            st.write('##### **Contract And Billing**')
            contract = st.selectbox('Contract:', options=['Month-to-Month', 'One year', 'Two years'], key = 'contract')
            paperless_billing = st.selectbox('PaperlessBilling:', options=['Yes', 'No', 'No internet service'], key = 'paperless_billing')
            payment_method = st.selectbox('PaymentMethod:', options=['Mailed Check', 'Electronic Check', 'Bank Transfer', 'Credit Card'], key = 'payment_method')
            

        with column5:
            st.write('##### **Financials**')
            monthly_charges = st.number_input('MonthlyCharges:', key= 'monthly_charges')
            total_charges = st.number_input('TotalCharges:', key = "total_charges")
            tenure = st.number_input('Tenure:', min_value=1, max_value=30, step=1, key= 'tenure')

        keys = [gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv,
               streaming_movies, contract, paperless_billing, payment_method, monthly_charges, total_charges]

        global submit
        submit = st.form_submit_button('Predict')

    if submit:
        st.write(test_df)
        with st.spinner("Prediction in progress. Please wait."):
            time.sleep(10)
            #st.write('#### :green[Prediction Complete. View results]')
            st.success('Prediction Complete. View results')




       

#         # Access the values directly from st.session_state
#         #inputs = {column: st.session_state[column] for column in selected_columns}
#         )
#         st.write(test_df)
#     else:
#         st.warning("Please select a model and fill out the form before predicting.")
            

    
    



def predict():
    # Function to predict and display result
    # Make prediction
    global test_df
    if st.session_state['predictor_choice'] == 'Logistic Regression':
        prediction_probabilities = log_reg.predict_proba(test_df)
        churn_probability = prediction_probabilities[0][1]
        make_predictions = log_reg.predict(test_df)
        make_predictions = encoder.inverse_transform(make_predictions)
    else:  # SGD Model
        prediction_probabilities = sgd_model.predict_proba(test_df)
        churn_probability = prediction_probabilities[0][1]
        make_predictions = sgd_model.predict(test_df)
        make_predictions = encoder.inverse_transform(make_predictions)
    return make_predictions


# Display results
results, visual = st.columns(2)
with results:
    pass
with visual:
    pass







if __name__ == "__main__":
    load_tools()
    model_pick()
    feature_inputs()
    input_save()
    