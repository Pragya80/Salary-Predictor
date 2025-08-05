# 💼 Salary-Predictor 

It predicts an employee's salary based on several key factors. The application uses a pre-trained machine learning model to provide an estimated salary, making it a useful tool for salary benchmarking and analysis.

🚀Features
Predicts salary based on user-defined inputs.

Interactive and user-friendly interface.

🧠Takes the following inputs:
1. Age
2. Gender
3. Education Level
4. Job Title
5. Years of Experience

How to Run Locally
To run this application on your local machine, follow these steps:

Clone the repository:

Bash

git clone [https://github.com/Pragya80/Salary-Predictor]
cd Salary-Predictor

Install dependencies:
Make sure you have Python installed. Then, install the required libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
Run the Streamlit app:

Bash

streamlit run app.py
Your application will open in a new tab in your web browser.

📁File Structure
app.py: The main Python script that contains the Streamlit application logic, user interface, and model prediction code.

salary_model.pkl: The pickled file containing the trained scikit-learn Linear Regression model used for salary prediction.

encoders.pkl: A single pickled file that stores all the LabelEncoder objects required to convert categorical input data into numerical values for the model.

requirements.txt: A text file listing all the Python libraries and their versions required to run the application.

💻Technologies Used
Streamlit: For building the interactive web application.

scikit-learn: For the machine learning model (LinearRegression) and data preprocessing (LabelEncoder).

NumPy: For handling numerical data.

🛫Deploy Link: https://pragya80-salary-predictor-app-fbhkad.streamlit.app/
