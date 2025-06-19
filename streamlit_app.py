
import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model and preprocessing objects
svm_model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")
le_study = joblib.load("le_study.pkl")
le_sleep = joblib.load("le_sleep.pkl")

# Define bin edges and labels for study and sleep
study_bins = [0, 2, 4, 6, 8, 10]
sleep_bins = [0, 4, 6, 8, 10, 12]
labels = ["Very Low", "Low", "Moderate", "High", "Very High"]

st.set_page_config(page_title="Student Stress Predictor", page_icon="📊")
st.title("📘 Student Stress Level Predictor")
st.write("Enter your daily habits to predict your likely stress level.")

# Input widgets
study_hours = st.slider("Study Hours Per Day", 0.0, 10.0, step=0.5)
sleep_hours = st.slider("Sleep Hours Per Day", 0.0, 12.0, step=0.5)
gpa = st.slider("GPA", 0.0, 4.0, step=0.01)

if st.button("Predict Stress Level"):
    # Bin inputs
    study_cat = pd.cut([study_hours], bins=study_bins, labels=labels)[0]
    sleep_cat = pd.cut([sleep_hours], bins=sleep_bins, labels=labels)[0]

    # Encode categories
    study_encoded = le_study.transform([study_cat])[0]
    sleep_encoded = le_sleep.transform([sleep_cat])[0]

    # Combine and scale features
    X_input = scaler.transform([[study_encoded, sleep_encoded, gpa]])

    # Predict
    prediction = svm_model.predict(X_input)[0]
    stress_map = {1: "Low", 2: "Moderate", 3: "High"}
    st.success(f"🎯 Predicted Stress Level: **{stress_map.get(prediction, 'Unknown')}**")
