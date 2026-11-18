
# 🛡️ ChurnShield – Customer Churn Prediction System

## Project Overview
ChurnShield is a Machine Learning-based customer churn prediction system that predicts whether a customer is likely to leave a telecommunications service.

The project uses a trained Gradient Boosting Classifier and a Streamlit interface to predict customer churn based on customer information, internet services, contract details and billing information.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit
- Joblib

## Machine Learning Workflow
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Handling Class Imbalance using SMOTE
6. Model Training and Hyperparameter Tuning
7. Model Evaluation
8. Model Saving using Pickle
9. Deployment using Streamlit

## Model Used
- Gradient Boosting Classifier

## Application Features
- Customer information input
- Service and billing details
- Churn probability prediction
- Customer retention recommendations

## Project Structure
- app.py – Streamlit application
- model.ipynb – Model development and analysis
- final_gb_classifier.pkl – Trained ML model
- Telco-Customer-Churn.csv – Dataset
- requirements.txt – Project dependencies

## How to Run the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Output
The application displays the predicted churn probability and indicates whether a customer is likely to churn or stay.
<img width="590" height="672" alt="Screenshot 2026-11-17 205140" src="https://github.com/user-attachments/assets/efc8d745-eb49-4fe2-a161-508db0b813b8" />
