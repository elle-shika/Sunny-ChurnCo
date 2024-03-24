# Sunny-ChurnCo
A Data App Project using Streamlit - Embedding Machine Learning Models in GUIs


## 🤓ChurnCo: 
 
The ChurnCo is an interactive Streamlit application designed to forecast customer churn based on Customer Churn data from a Telco. This README provides offers detailed guidelines for developing, deploying, and using  the app.
 
### 📜Table of Contents
1. [⚙️Setup](#setup)
2. [🧱Prerequisites](#Prerequisites)
3. [Running the App](#running-the-app)
4. [Usage](#usage)
    - [🏡Home Page](#home-page)
    - [🔢Data Page](#data-page)
    - [📊Dashboard Page](#dashboard-page)
    - [🎰Predictor Page](#predictor-page)
    - [⌛History Page](#history-page)
5. [🤖Models Used](#models-used)
6. [🚀Deployment](#deployment)
7. [Further Development](#further-development)
8. 📄[Documentation](#Documentation)
9. [🤝Contributing](#contributing)
10. [👩‍💻Author](#author)
11. [🏅License](#license)
 
### ⚙️Setup <a name="setup"></a>
 
1. **Clone Repository**: Clone the repository containing the Streamlit app code.
2. **Install Dependencies**: Install the required dependencies using pip.
3. **Data Setup**: Ensure you have a CSV dataset named `Churn Prediction Dataset.csv` placed inside a folder named `assets` in the project directory.
4. **Configuration**: Update the `.env` file with necessary credentials and configuration details.
 
### 🧱Prerequisites <a name="prerequisites"></a>

To be able to set-up and run this app, you would need:
- [git](https://git-scm.com/downloads) for cloning of source code onto your device.
- [VS Code](https://code.visualstudio.com/download) for running and editing of source code.

### Running the App <a name="running-the-app"></a>
 
To set the app running locally, run the following command within the project directory:
 
```bash
streamlit run 🏡Home.py
```
 
The app will then be accessible through a web browser on your local machine.
 
### Usage <a name="usage"></a>
 
#### 🏡Home Page <a name="home-page"></a>
- Provides an overview of the app and its purpose after a successful log in.
 
#### 🔢Data Page <a name="data-page"></a>
- Allows for selecting a source of data (either from in-built data or an uploaded csv of similar structure to in-built data)
- Provides Preview of the first few rows of the dataset.
- Shows summary info on structure of data.
- Displays basic information about the dataset.

#### 📊Dashboard Page <a name="dashboard-page"></a>
- Offers insights through various charts and plots.
- Provides visualizations on the various features in the customer churn data.
- Summary visuals of research questions and key performance indicators.

 
#### 🎰Predictor Page <a name="predictor-page"></a>
- Allows input customer details interactively to predict churn.
 
#### ⌛History Page <a name="history-page"></a>
- Tracks user interactions with the app.
- Displays a history log of actions performed by the user.
 
### 🤖Models Used <a name="models-used"></a>
 
#### Supported Models
1. Logistic Regression Model
2. Stochastic Gradient Descent for Logistic Regression (SGD)
 
#### Description
- Logistic Regression: A supervised machine learning algorithm for classification by calculating the probability of an instance.
- SGD: Optimization algorithm for training logistic regression models

 
### 🚀Deployment <a name="deployment"></a>
 
- Model Serialization
- Model Loading
 
### Further Development <a name="further-development"></a>
 
- Model Tuning
- Model Expansion
- Model Monitoring

### 📄Documentation <a name="documentation"></a>
 Medium:
 
### 🤝Contributing <a name="contributing"></a>
 
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.

### 👩‍💻Author <a name="author"></a>
Coder Michelle Pamela
- GitHub: [Elle-shika](https://github.com/elle-shika)
- LinkedIn: [michelle-pamela](www.linkedin.com/in/michelle-pamela)
 
### 🏅License <a name="license"></a>
 
This project is licensed under the [MIT license](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.
















 

