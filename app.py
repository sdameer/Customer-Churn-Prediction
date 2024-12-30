import streamlit as st
import numpy as np
import pickle  # Assume the model is saved using pickle

# Load the trained model (replace 'final_model.pkl' with your actual model filename)
with open('customer.pickle', 'rb') as file:
    final_model = pickle.load(file)

# Define the app
def main():
    st.title("Customer Churn Prediction")

    st.sidebar.header("Input Features")

    # Input fields for the features
    gender = st.sidebar.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    senior_citizen = st.sidebar.selectbox("Senior Citizen", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    partner = st.sidebar.selectbox("Partner", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    dependents = st.sidebar.selectbox("Dependents", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    tenure = st.sidebar.slider("Tenure (months)", min_value=1, max_value=72, value=1)
    phone_service = st.sidebar.selectbox("Phone Service", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    multiple_lines = st.sidebar.selectbox("Multiple Lines", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No phone service"))
    internet_service = st.sidebar.selectbox("Internet Service", options=[0, 1, 2], format_func=lambda x: "DSL" if x == 1 else ("Fiber Optic" if x == 2 else "No"))
    online_security = st.sidebar.selectbox("Online Security", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    online_backup = st.sidebar.selectbox("Online Backup", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    device_protection = st.sidebar.selectbox("Device Protection", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    tech_support = st.sidebar.selectbox("Tech Support", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    streaming_tv = st.sidebar.selectbox("Streaming TV", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    streaming_movies = st.sidebar.selectbox("Streaming Movies", options=[0, 1, 2], format_func=lambda x: "Yes" if x == 1 else ("No" if x == 0 else "No internet service"))
    contract = st.sidebar.selectbox("Contract", options=[0, 1, 2], format_func=lambda x: "Month-to-Month" if x == 0 else ("One Year" if x == 1 else "Two Year"))
    paperless_billing = st.sidebar.selectbox("Paperless Billing", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    payment_method = st.sidebar.selectbox("Payment Method", options=[0, 1, 2, 3], format_func=lambda x: ["Electronic Check", "Mailed Check", "Bank Transfer", "Credit Card"][x])
    monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=0.0, step=0.01)
    total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, value=0.0, step=0.01)

    # Prediction button
    if st.sidebar.button("Predict Churn"):
        # Prepare the input data as a NumPy array
        input_data = np.array([[
            gender, senior_citizen, partner, dependents, tenure,
            phone_service, multiple_lines, internet_service, online_security,
            online_backup, device_protection, tech_support, streaming_tv,
            streaming_movies, contract, paperless_billing, payment_method,
            monthly_charges, total_charges
        ]])

        # Make prediction
        prediction = final_model.predict(input_data)[0]

        # Display result
        st.write("### Prediction Result")
        st.write("<h2>The customer is likely to <strong>Churn: Yes</strong>.</h2>" if prediction == 1 else "<h2>The customer is likely to <strong>Churn: No</strong>.</h2>", unsafe_allow_html=True)

    # Footer section
    st.write("---")
    st.write("## Connect with Me:")
    st.write("**Project Code:** [Kaggle](https://www.kaggle.com/code/sdameer/customer-churn-prediction/), [GitHub](https://github.com/sdameer/Customer-Churn-Prediction/)")
    st.write("**GitHub Profile:** [github.com/sdameer](https://github.com/sdameer)")
    st.write("**LinkedIn:** [linkedin.com/in/sdameer](https://linkedin.com/in/sdameer)")

if __name__ == "__main__":
    main()

# Connections section
st.write("---")
st.write("**Connections:** [Connect on LinkedIn](https://linkedin.com/in/sdameer)")
