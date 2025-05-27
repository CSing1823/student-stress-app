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
- **XGBoost Classifier**
- **Support Vector Machine (SVM) with RBF kernel** – *Best performing model*

Each model was evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score (Macro-Averaged)**

The SVM with RBF kernel showed the highest performance across most metrics, effectively handling nonlinear decision boundaries in our dataset.

### 5️⃣ **Interpret**
The model outputs were analyzed to identify behavioral patterns that contribute to high stress levels among students:

- **High Stress Indicators**: Students with **long study hours** (e.g., >6 hours/day) and **short sleep duration** (e.g., <5 hours/day) were more likely to be classified as experiencing high stress.
- **Moderate Stress**: Typically observed in students with a mix of average study hours and reduced sleep.
- **Low Stress**: Common among students who maintained a balanced routine with **moderate study time** and **sufficient sleep** (7–8 hours/day).

Based on these findings, we provided **practical recommendations** for stress management:
- Prioritize consistent sleep schedules.
- Avoid overstudying at the expense of rest.
- Adopt a balanced approach to academic workloads and self-care.

These insights are made actionable through our deployed web application:  
👉 **[Try the Stress Level Predictor Web App](https://your-streamlit-app-link.streamlit.app/)**

This tool allows users to input their daily study hours, sleep duration, and GPA to receive an instant prediction of their stress level.

---

## 🧠 Best Model

After training and evaluating five classification models, the **Support Vector Machine (SVM) with RBF Kernel** achieved the best overall performance across all key metrics.

| Model                 | Accuracy | Macro F1-Score | F1 (Low) | F1 (Moderate) | F1 (High) |
|----------------------|----------|----------------|----------|----------------|-----------|
| Random Forest        | 0.94     | 0.92           | 0.85     | 0.93           | 0.98      |
| Logistic Regression  | 0.82     | 0.82           | 0.79     | 0.85           | 0.82      |
| K-Nearest Neighbors  | 0.97     | 0.96           | 0.94     | 0.95           | 0.98      |
| XGBoost Classifier   | 0.95     | 0.93           | 0.87     | 0.93           | 0.98      |
| **SVM (RBF Kernel)** | **0.97** | **0.97**       | **0.95** | **0.97**       | **0.99**  |

💡 **Why SVM was selected**:
- It achieved the **highest scores across all metrics**, including F1-scores for each class.
- Especially strong at identifying underrepresented classes such as “Moderate” stress.

🧪 **Deployment**:
- The trained SVM model was exported using `joblib` and integrated into the deployed web app.
- Users can enter their daily study hours, sleep hours, and GPA to predict their stress level.
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
