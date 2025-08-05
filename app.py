
import streamlit as st
import pickle
import numpy as np

# Load model and all encoders from a single file
@st.cache_resource
def load_assets():
    # Load the model
    with open("salary_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Load all encoders as a single object from the file
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    
    return model, encoders[0], encoders[1], encoders[2]

# Load the model and encoders
model, le_gender, le_edu, le_job = load_assets()

# Streamlit UI
st.title("💼 Employee Salary Predictor")
st.write("Predict salary based on age, gender, education, job title, and experience.")

# User input
age = st.slider("Age", 18, 65, 25)
gender = st.selectbox("Gender", le_gender.classes_)
edu = st.selectbox("Education Level", le_edu.classes_)
job = st.selectbox("Job Title", le_job.classes_)
exp = st.slider("Years of Experience", 0, 40, 2)

if st.button("Predict Salary"):
    try:
        input_data = np.array([[
            age,
            le_gender.transform([gender])[0],
            le_edu.transform([edu])[0],
            le_job.transform([job])[0],
            exp
        ]])
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Salary: ₹ {int(prediction):,}")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
