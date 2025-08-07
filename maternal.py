# Streamlit App for Maternal Health Risk Prediction

import streamlit as st
import numpy as np
import joblib

# Load the trained Extra Trees model
model = joblib.load("extra_trees_model.pkl")

st.set_page_config(page_title="Maternal Health Risk Predictor", layout="centered")
st.title("Maternal Health Risk Prediction")
st.write(
    """
    This app predicts the risk level (Low, Mid, High) for maternal health based on clinical parameters.
    Please enter the required information below:
    """
)

# Sidebar for user input
st.sidebar.header("Input Features")


def user_input_features():
    age = st.sidebar.slider("Age (years)", 10, 70, 30)
    systolic_bp = st.sidebar.slider("Systolic Blood Pressure (mmHg)", 80, 200, 120)
    diastolic_bp = st.sidebar.slider("Diastolic Blood Pressure (mmHg)", 40, 130, 80)
    blood_glucose = st.sidebar.slider("Blood Glucose (mmol/L)", 2, 20, 5)
    body_temp = st.sidebar.slider("Body Temperature (°C)", 30.0, 43.0, 36.5)
    heart_rate = st.sidebar.slider("Heart Rate (bpm)", 50, 180, 80)
    data = {
        "Age": age,
        "SystolicBP": systolic_bp,
        "DiastolicBP": diastolic_bp,
        "BloodGlucose": blood_glucose,
        "BodyTemp": body_temp,
        "HeartRate": heart_rate,
    }
    features = np.array([list(data.values())])
    return features, data


features, input_data = user_input_features()

st.subheader("Entered Information")
st.write(input_data)

if st.button("Predict Risk Level"):
    prediction = model.predict(features)[0]
    risk_map = {0: "Low Risk", 1: "Mid Risk", 2: "High Risk"}
    risk_color = {0: "green", 1: "orange", 2: "red"}
    st.markdown(
        f"### Predicted Maternal Health Risk Level: "
        f"<span style='color:{risk_color[prediction]};font-weight:bold'>{risk_map[prediction]}</span>",
        unsafe_allow_html=True,
    )
    st.info("Please consult a healthcare professional for further advice.")

st.markdown("---")
st.caption("Powered by Extra Trees Classifier | MaternalWatch AI")
