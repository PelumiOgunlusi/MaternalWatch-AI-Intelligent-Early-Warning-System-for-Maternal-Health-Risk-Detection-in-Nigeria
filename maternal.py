# Streamlit App for Maternal Health Risk Prediction

import streamlit as st
import numpy as np
import joblib
import smtplib
from email.mime.text import MIMEText

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


st.sidebar.header("Hospital Alert Details")
hospital_name = st.sidebar.text_input("Nearest Maternity Hospital Name")
hospital_email = st.sidebar.text_input("Hospital Contact Email")
patient_phone = st.sidebar.text_input("Your Phone Number")


def send_alert_email(hospital, email, patient_data, phone):
    subject = "High Risk Maternal Health Alert"
    body = (
        f"Alert: A patient has been assessed as HIGH RISK for maternal health complications.\n\n"
        f"Nearest Hospital: {hospital}\n"
        f"Patient Data: {patient_data}\n\n"
        f"Patient Phone Number: {phone}\n\n"
        "Please prepare for possible emergency care and contact the patient as soon as possible."
    )
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "alert@maternalwatch.ai"
    msg["To"] = email

    try:
        # Example using Gmail SMTP server (replace with your credentials)
        # Make sure to enable 2-Step Verification on your Google account and generate an App Password.
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "pelumiogunlusi@gmail.com"  # Replace with your Gmail address
        sender_password = "ezbp ejiw lngf tcmk"  # Replace with your generated App Password from Google Account settings

        msg["From"] = sender_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Failed to send alert email: {e}")
        return False


if "prediction" in locals() and prediction == 2:
    if hospital_name and hospital_email and patient_phone:
        if send_alert_email(hospital_name, hospital_email, input_data, patient_phone):
            st.success(
                f"Alert sent to {hospital_name} ({hospital_email}) for High Risk case."
            )
    else:
        st.warning(
            "Please provide the hospital name, email, and your phone number to enable alert notifications."
        )
