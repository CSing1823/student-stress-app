
import streamlit as st
import numpy as np
import joblib

# Load model and scaler
svm_model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Student Stress Predictor", page_icon="📊")
st.title("📘 Student Stress Level Predictor")
st.write("Enter your daily habits to predict your likely stress level.")

# Input widgets
study_hours = st.slider("Study Hours Per Day", 0.0, 10.0, step=0.5)
sleep_hours = st.slider("Sleep Hours Per Day", 0.0, 12.0, step=0.5)
gpa = st.slider("GPA", 0.0, 4.0, step=0.01)

if st.button("Predict Stress Level"):
    # Scale input features directly
    X_input = scaler.transform([[study_hours, sleep_hours, gpa]])

    # Predict stress level
    prediction = svm_model.predict(X_input)[0]  # Directly outputs "Low", "Moderate", or "High"
    
    st.success(f"🎯 Predicted Stress Level: **{prediction}**")
    