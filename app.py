import streamlit as st
import pickle
import numpy as np

# Load model and encoders separately
@st.cache_resource
def load_model():
    with open("salary_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

@st.cache_resource
def load_encoder(path):
    with open(path, "rb") as f:
        encoder = pickle.load(f)
    return encoder

model = load_model()
le_gender = load_encoder("le_gender.pkl")
le_edu = load_encoder("le_edu.pkl")
le_job = load_encoder("le_job.pkl")

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
