# import necessary packages
import json
import streamlit as st
from streamlit_lottie import st_lottie
import time
import datetime
import os
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
def load_log():
    log_reg = joblib.load('.\model\Churn_Predictor.joblib') #load  logistic regression model
    return log_reg
def load_sgd():
    sgd_model = joblib.load('.\model\Churn_SGD_Predictor.joblib') # load SGD model
    return sgd_model
def load_tool():
    encoder = joblib.load('.\model\Encoder.joblib') # load encoder
    return encoder

    

def model_pick():
    column1, column2 = st.columns(2)
    with column1:
        # function allowing user to select a prediction model
        st.selectbox(label= '**Select your predictor.**', options =['Logistic Regression', 'SGD'], key = 'predictor_choice')

    with column2:
        # insert an animation or image
        pass





def feature_inputs():
    # Function to collect features inputs from user
    st.write('**Enter description of Customer you want to assess.**') 
 
    
    with st.form('Customer_information'):
        column1, column2, column3, column4, column5 = st.columns(5)
        with column1:
            st.write('##### **Personal Details**')
            gender = st.selectbox('Gender:', options=['Male', 'Female'], key = 'gender')
            senior_citizen = st.number_input('SeniorCitizen [Yes = 1 and No = 0]:',  min_value=0, max_value=1, step=1, key = 'senior_citizen')
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
            contract = st.selectbox('Contract:', options=['Month-to-month', 'One year', 'Two years'], key = 'contract')
            paperless_billing = st.selectbox('PaperlessBilling:', options=['Yes', 'No', 'No internet service'], key = 'paperless_billing')
            payment_method = st.selectbox('PaymentMethod:', options=['Mailed check', 'Electronic check', 'Bank transfer(automatic)', 'Credit card(automatic)'], key = 'payment_method')
            

        with column5:
            st.write('##### **Financials**')
            tenure = st.number_input('Tenure:', min_value=1, max_value=30, step=1, key= 'tenure')
            monthly_charges = st.number_input('MonthlyCharges:', key= 'monthly_charges')
            total_charges = st.number_input('TotalCharges:', key = "total_charges")
            

        global submit
        submit = st.form_submit_button(label = 'Predict', on_click= input_save)

    if submit:
        with st.spinner("Prediction in progress. Please wait."):
            time.sleep(10)
        st.success('Prediction Complete. View results')


def input_save():
    # function to save all user input as a test dataframe
        # retrieve inputs from session state

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
    test_df = pd.DataFrame(inputs,columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService','MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
                        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'])
    st.write(test_df)
    # # Reset index
    # test_df_reset = test_df.reset_index(drop=True)

    # # Access 'tenure' column
    # tenure_column = test_df_reset['tenure']

    # st.write(test_df)
    test_df['Prediciton Time'] = datetime.date.today()
    test_df['Model Used'] = st.session_state['predictor_choice']


    test_df.to_csv('./history.csv', mode='a', header=not os.path.exists('./history.csv'), index=False)


    # Function to predict and display result
    # Make prediction
    if st.session_state['predictor_choice'] == 'Logistic Regression':
        log_reg = load_log()
        prediction_probabilities = log_reg.predict_proba(test_df)
        churn_probability = prediction_probabilities[0][1]
        make_predictions = log_reg.predict(test_df)
        encoder = load_tool()
        make_predictions = encoder.inverse_transform(make_predictions)
    else:  
        # SGD Model
        sgd_model = load_sgd()
        prediction_probabilities = sgd_model.predict_proba(test_df)
        churn_probability = prediction_probabilities[0][1]
        make_predictions = sgd_model.predict(test_df)
        encoder = load_tool()
        make_predictions = encoder.inverse_transform(make_predictions)

        st.session_state['make_predictions'] = make_predictions
        st.session_state['churn_probability'] = churn_probability

    return make_predictions, churn_probability
    
 
if 'make_predictions' not in st.session_state:
    st.session_state['make_predictions'] = None 
if 'churn_probability' not in st.session_state:
    st.session_state['churn_probability'] = None


# def load_lottiefile(filepath):
#     with open(filepath, "r") as f:
#         return json.load(f)
    

def display_results():
    col6, col7 = st.columns(2)
    prediction = st.session_state['make_predictions']
    probability = st.session_state['churn_probability']
    

    with col6:
        if prediction == 'Yes':
            lottie_churn = json.load(r'./Animation - churn.json')
            st_lottie(lottie_churn)
        elif prediction == 'No':
            lottie_nochurn = json.load(r'./Animation - nochurn.json')
            st_lottie(lottie_nochurn)

    with col7:
        if prediction == 'Yes':
            st.write(f'This customer will churn at a probabilty of {probability[0][1] * 100}')

        elif prediction == 'No':
            st.write(f'This customer will not churn at a probabilty of {probability[0][1] * 100}')    

if __name__ == "__main__":
    load_log()
    load_sgd()
    load_tool()
    model_pick()
    feature_inputs()

# Check if predictions have been made before displaying results
#if st.session_state['make_predictions'] is not None:
st.write(st.session_state['churn_probability'])
st.write(st.session_state['predictor_choice']) 

