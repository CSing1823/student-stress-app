# 🎓 student-stress-app

A **Streamlit-based web app** that predicts student stress levels based on their **daily study hours**, **sleep duration**, and **GPA**.  
Built for the **WIE2003 Introduction to Data Science** assignment using a machine learning pipeline with **SVM Classification**.

---

## 📊 Project Overview

This project aims to develop a predictive model that estimates a student's stress level (Low, Moderate, High) using daily behavior patterns. It is designed as both an academic exploration and a practical tool to raise awareness about student well-being.

---

## 🔍 Data Analysis Workflow (OSEMN Framework)

### 1️⃣ **Obtain**
We obtained the dataset from Kaggle: [Student Lifestyle Dataset](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset), which includes anonymized responses from **2,000 university students**.

The dataset contains the following key variables:

- **Study_Hours_Per_Day**: Number of hours a student studies daily  
- **Sleep_Hours_Per_Day**: Average daily sleep duration  
- **GPA**: Reported academic performance on a 4.0 scale  
- **Stress_Level**: Self-reported stress classified as *Low*, *Moderate*, or *High*

Collected via Google Forms, this survey-based dataset offers insight into how academic behaviors and lifestyle factors influence student stress levels. Despite some potential for subjective bias, its clean structure and large sample size make it highly suitable for exploratory and predictive analysis.

### 2️⃣ **Scrub**
The dataset was examined for quality issues and prepared for analysis through the following steps:

- **Missing Values**: Checked all columns for null or inconsistent values. The dataset was clean—no missing or duplicate entries were found.
- **Data Type Conversion**: Categorical variable `Stress_Level` was encoded as numerical values (`Low` → 0, `Moderate` → 1, `High` → 2) to support machine learning models.
- **Binning**: Continuous variables such as `Study_Hours_Per_Day` and `Sleep_Hours_Per_Day` were binned into categorical levels like `Very Low`, `Low`, `Moderate`, `High`, and `Very High` for more interpretable visualizations and subgroup analysis.
- **Outliers**: Visual and statistical checks showed all values were within acceptable, realistic ranges. No outliers were removed.

These preprocessing steps ensured the data was structured, consistent, and ready for analysis and modeling.

### 3️⃣ **Explore**
We conducted Exploratory Data Analysis (EDA) to uncover trends, correlations, and patterns in the dataset:

- **Correlation Analysis**: Used heatmaps and scatter plots to explore relationships between `Study_Hours_Per_Day`, `Sleep_Hours_Per_Day`, `GPA`, and `Stress_Level`.
- **Visualizations**: Applied histograms, KDE plots, pairplots, and bar charts to examine variable distributions and stress level variations across different lifestyle patterns.
- **Key Insights**:
  - Higher study hours are associated with increased stress.
  - Lower sleep duration correlates with higher stress.
  - High GPA students also report higher stress levels, suggesting pressure to maintain performance.

This phase helped shape hypotheses and informed the feature selection for the modeling stage.

### 4️⃣ **Model**
To address class imbalance in the `Stress_Level` variable, we applied **SMOTE** (Synthetic Minority Over-sampling Technique) to the training set. This helped ensure fair representation of all stress categories during model training.

We trained and evaluated the following five classification models:

- **Random Forest**
- **Logistic Regression**
- **K-Nearest Neighbors (KNN)**
- **XGBoost**
- **Support Vector Machine (SVM) with RBF kernel** – *Best performing model*

Each model was evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score (Macro-Averaged)**

The SVM with RBF kernel showed the highest performance across most metrics, effectively handling nonlinear decision boundaries in our dataset.

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

Developed by See Chan Sing as part of **WIE2003 Introduction to Data Science** coursework at **University of Malaya**.
