# 🎓 student-stress-app

A **Streamlit-based web app** that predicts student stress levels based on their **daily study hours**, **sleep duration**, and **GPA**.  
Built for the **WIE2003 Introduction to Data Science** assignment using a machine learning pipeline with **SVM Classification**.

---

## 📊 Project Overview

This project aims to develop a predictive model that estimates a student's stress level (Low, Moderate, High) using daily behavior patterns. It is designed as both an academic exploration and a practical tool to raise awareness about student well-being.

---

## 🔍 Data Analysis Workflow (OSEMN Framework)

### 1️⃣ **Obtain**
- Collected survey data on students' daily **Study Hours**, **Sleep Hours**, **GPA**, and **self-reported Stress Levels**.

### 2️⃣ **Scrub**
- Cleaned missing or inconsistent values.
- Binned numeric variables (e.g., `Study_Hours_Per_Day` and `Sleep_Hours_Per_Day`) into categories like `Low`, `Moderate`, `High`.

### 3️⃣ **Explore**
- Conducted exploratory data analysis (EDA).
- Visualized the **correlation between study/sleep habits and stress**.
- Tested hypotheses on behavior patterns and stress outcomes.

### 4️⃣ **Model**
- Applied **SMOTE** to balance the class distribution.
- Trained 5 models:
  - Random Forest  
  - Logistic Regression  
  - K-Nearest Neighbors (KNN)  
  - XGBoost  
  - **SVM with RBF kernel** (Best performing model)

- Evaluated performance using **Accuracy**, **Precision**, **Recall**, and **F1-Score**.

### 5️⃣ **Interpret**
- Identified key behavioral indicators of high stress (e.g., high study hours + low sleep).
- Offered practical recommendations for stress management and lifestyle balance.

---

## 🧠 Best Model

- **Support Vector Machine (SVM)** with **RBF Kernel** achieved the highest macro F1-score.
- This model was exported using `joblib` and integrated into the web app.

---

## 🌐 Deployed Web App

Access the Student Stress Level Predictor [here](https://student-stress-app-vngkjyolzxxx7kqtbeuztr.streamlit.app)

---

## 📁 Files Included

| File                | Description                                |
|---------------------|--------------------------------------------|
| `svm_model.pkl`     | Final trained SVM model                    |
| `scaler.pkl`        | StandardScaler used to normalize inputs    |
| `le_study.pkl`      | Label encoder for study categories         |
| `le_sleep.pkl`      | Label encoder for sleep categories         |
| `requirements.txt`  | Python dependencies for Streamlit app      |
| `streamlit_app.py`  | Main script to launch the web application |
| `WIE2003_IDS_Assignment.ipynb` | Full data science analysis notebook |

---

## 📢 Credits

Developed by [Your Name] as part of **WIE2003 Introduction to Data Science** coursework at **University of Malaya**.
