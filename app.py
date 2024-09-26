import streamlit as st
import joblib
import numpy as np
import sklearn


# Load the model and scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Heart Disease Prediction App")


# Create tabs for input
age = st.number_input("Age", min_value=1, max_value=100, value=40)
sex = st.selectbox("Sex (0: Female, 1: Male)", [0, 1])
chest_pain = st.number_input("Chest Pain Type (1-4)", min_value=1, max_value=4, value=2)
resting_bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=400, value=200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)", [0, 1])
resting_ecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2, value=0)
max_heart_rate = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina (0: No, 1: Yes)", [0, 1])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.number_input("ST Slope (1-3)", min_value=1, max_value=3, value=2)

# Make prediction
if st.button("Predict"):
    features = np.array([[age, sex, chest_pain, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg,
                          max_heart_rate, exercise_angina, oldpeak, st_slope]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    st.write("Prediction (0: No Heart Disease, 1: Heart Disease):", int(prediction[0]))