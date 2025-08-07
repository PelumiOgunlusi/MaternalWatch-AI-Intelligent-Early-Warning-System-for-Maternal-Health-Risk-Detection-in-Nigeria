# MaternalWatch AI: Intelligent Early Warning System for Maternal Health Risk Detection in Nigeria
## Overview

MaternalWatch AI is a digital health platform leveraging artificial intelligence and machine learning to provide real-time maternal health risk assessment and early warning capabilities for pregnant women in Nigeria. This project demonstrates the end-to-end process of building a predictive model for maternal health risk using real-world data, including data cleaning, exploratory analysis, feature engineering, model training, evaluation, interpretation, and deployment.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Project Walkthrough](#project-walkthrough)
    - [1. Data Inspection & Cleaning](#1-data-inspection--cleaning)
    - [2. Exploratory Data Analysis (EDA)](#2-exploratory-data-analysis-eda)
    - [3. Feature Engineering & Encoding](#3-feature-engineering--encoding)
    - [4. Data Balancing](#4-data-balancing)
    - [5. Model Training & Evaluation](#5-model-training--evaluation)
    - [6. Model Comparison](#6-model-comparison)
    - [7. Model Interpretation](#7-model-interpretation)
    - [8. Model Deployment](#8-model-deployment)
    - [9. Streamlit Web Application](#9-streamlit-web-application)
- [Results & Insights](#results--insights)
- [References](#references)

---

## Problem Statement

Nigeria faces a severe maternal health crisis, with high maternal mortality rates due to inadequate healthcare infrastructure, limited access to skilled providers, and poor early detection of high-risk pregnancies. MaternalWatch AI aims to address these challenges by providing predictive analytics and real-time monitoring to enable timely interventions.

---

## Dataset

- **Source:** [Kaggle - Maternal Health Risk Data Set](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data/data)
- **Features:**
    - Age
    - SystolicBP
    - DiastolicBP
    - BloodGlucose
    - BodyTemp
    - HeartRate
    - RiskLevel (target: low, mid, high risk)

---

## Project Structure

- `MarternalWatchAI.qmd`: Main Quarto notebook containing all code, analysis, and documentation.
- `data/Maternal Health Risk Data Set.csv`: Dataset file.
- `extra_trees_model.pkl`: Saved trained model for deployment.

---

## Installation

1. **Clone the repository**
     ```
     git clone https://github.com/<your-username>/MaternalWatch-AI-Intelligent-Early-Warning-System-for-Maternal-Health-Risk-Detection-in-Nigeria.git
     cd MaternalWatch-AI-Intelligent-Early-Warning-System-for-Maternal-Health-Risk-Detection-in-Nigeria
     ```

2. **Install required Python libraries**
     ```
     pip install pandas numpy seaborn matplotlib plotly itables scikit-learn imbalanced-learn shap joblib
     ```

3. **Download the dataset**
     - Place `Maternal Health Risk Data Set.csv` in the `data/` directory.

---

## Project Walkthrough

### 1. Data Inspection & Cleaning

- Load the dataset and inspect its structure, data types, missing values, and duplicates.
- Remove duplicate rows (over 55% duplicates).
- Fix erroneous values (e.g., HeartRate value of 7 replaced with mode).
- Convert BodyTemp from Fahrenheit to Celsius.

### 2. Exploratory Data Analysis (EDA)

- Visualize distributions of features (histograms, boxplots).
- Analyze relationships between features and the target (pairplots, scatterplots, correlation heatmap).
- Identify outliers and feature-target associations.

### 3. Feature Engineering & Encoding

- Encode the ordinal target variable `RiskLevel` (low=0, mid=1, high=2).
- Separate features (`x`) and target (`y`).

### 4. Data Balancing

- Address class imbalance using `RandomOverSampler` from `imblearn`.
- Visualize the balanced class distribution.

### 5. Model Training & Evaluation

- Split data into training and test sets.
- Train and evaluate multiple models:
    - Support Vector Classifier (SVC)
    - K-Nearest Neighbors (KNN)
    - Decision Tree (with hyperparameter tuning)
    - Random Forest
    - Gradient Boosting
    - Extra Trees Classifier
- Evaluate models using accuracy, confusion matrix, and classification report.

### 6. Model Comparison

- Compare model performance and visualize results.
- Select the best-performing model (Extra Trees Classifier).

### 7. Model Interpretation

- Use SHAP to interpret feature importance for the Extra Trees model.
- Visualize SHAP summary plots for insights into feature contributions.

### 8. Model Deployment

- Save the trained Extra Trees model using `joblib` for future predictions and integration.

### 9. Streamlit Web Application

- Developed an interactive Streamlit web app for real-time maternal health risk prediction.
- The app allows users to input patient data and instantly receive risk assessments using the trained Extra Trees model.
- The web interface performs data preprocessing, prediction, and displays results and feature explanations dynamically.
- To run the app locally:
    ```
    pip install streamlit
    streamlit run maternal.py
    ```
- The app is also deployed online for broader accessibility and integration into healthcare workflows which is available [here](https://maternalwatchai.streamlit.app/).

---
## Results & Insights

- **Best Model:** Extra Trees Classifier (highest test accuracy).
- **Key Features:** Age, BloodGlucose, SystolicBP, DiastolicBP, BodyTemp, HeartRate.
- **Insights:**
    - High blood glucose and blood pressure are strong indicators of high-risk pregnancies.
    - Older age (>35) is associated with higher risk.
    - The model enables early identification of high-risk cases, supporting timely interventions.

---

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data/data)
- [Statista - Birth Rate for US Girls Aged 10-14](https://www.statista.com/statistics/410744/birth-rate-for-us-girls/)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)

---

## Contact

For questions or collaboration, please contact [PELUMI OGUNLUSI](mailto:your-email@example.com).

---

**Note:** This project is for educational and research purposes. For clinical use, further validation and regulatory approval are required.



