import streamlit as st
import pickle
import numpy as np

# Load model and encoders
with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    le_gender, le_edu, le_job = pickle.load(f)

# Streamlit UI
st.title("Employee Salary Prediction")
st.write("🔮 Predict the salary based on employee details")

# User inputs
age = st.slider("Age", 18, 65, 25)
gender = st.selectbox("Select Gender", le_gender.classes_)
edu = st.selectbox("Select Education Level", le_edu.classes_)
job = st.selectbox("Select Job Title", le_job.classes_)
exp = st.slider("Years of Experience", 0, 40, 1)

if st.button("Predict Salary"):
    # Transform input
    input_data = np.array([[
        age,
        le_gender.transform([gender])[0],
        le_edu.transform([edu])[0],
        le_job.transform([job])[0],
        exp
    ]])

    # Make prediction
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: ₹ {int(prediction):,}")
