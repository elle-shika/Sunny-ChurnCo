# import necessary packages
import streamlit as st
import time
import joblib


# set page configurations
st.set_page_config(
    page_title= "Let's Predict",
    layout = 'wide'
)
st.title('Customer Churn Prediction')


# load prediction models
st.cache_resource() #cache churn prediction models
def load_predictors():
    log_reg = joblib.load('\model\Churn_Predictor.joblib') #load  logistic regression model
    sgd_model = joblib.load('\model\Churn_SGD_Predictor.joblib') # load SGD model
    return log_reg, sgd_model


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
            gender = st.selectbox('Gender:', options=['Male', 'Female'])
            senior_citizen = st.selectbox('SeniorCitizen:', options=['Yes', 'No'])
            partner = st.selectbox('Partner:', options=['Yes', 'No'])
            dependents = st.selectbox('Dependents:', options=['Yes', 'No'])
            
 
        with column2:
            st.write('##### **Products And Services**')
            phone_service = st.selectbox('PhoneService:', options=['Yes', 'No'])
            multiple_lines = st.selectbox('MultipleLines:', options=['Yes', 'No', 'No phone service'])
            internet_service = st.selectbox('InternetService:', options=['DSL', 'Fiber Optic', 'No internet service'])
            device_protection = st.selectbox('DeviceProtection:', options=['Yes', 'No', 'No internet service'])
            tech_support = st.selectbox('TechSupport:', options=['Yes', 'No', 'No internet service'])
           
 
        with column3:
            st.write('##### **Online Services**')
            online_security = st.selectbox('OnlineSecurity:', options=['Yes', 'No', 'No internet service'])
            online_backup = st.selectbox('OnlineBackup:', options=['Yes', 'No', 'No internet service'])
            streaming_tv = st.selectbox('StreamingTv:', options=['Yes', 'No', 'No internet service'])
            streaming_movies = st.selectbox('StreamingMovies:', options=['Yes', 'No', 'No internet service'])
 
        with column4:
            st.write('##### **Contract And Billing**')
            contract = st.selectbox('Contract:', options=['Month-to-Month', 'One year', 'Two years'])
            paperless_billing = st.selectbox('PaperlessBilling:', options=['Yes', 'No', 'No internet service'])
            payment_method = st.selectbox('PaymentMethod:', options=['Mailed Check', 'Electronic Check', 'Bank Transfer', 'Credit Card'])
            

        with column5:
            st.write('##### **Financials**')
            monthly_charges = st.number_input('MonthlyCharges:')
            total_charges = st.number_input('TotalCharges:')
            tenure = st.number_input('Tenure:', min_value=1, max_value=30, step=1)

        submit = st.form_submit_button('Predict')

    if submit:
         with st.spinner("Prediction in progress. Please wait."):
            time.sleep(10)
            #st.write('#### :green[Prediction Complete. View results]')
            st.success('Prediction Complete. View results')

if __name__ == "__main__":
    model_pick()
    feature_inputs()