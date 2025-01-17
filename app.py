import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("rf_best_model.pkl")

# Define the selected features
selected_features = [
    'x.perimeter_worst',
    'x.area_worst',
    'x.radius_worst',
    'x.concave_pts_worst',
    'x.perimeter_mean'
]

# Streamlit app
st.title("Breast Cancer Prediction App")
st.write("Enter the feature values below to determine the health status:")

# Collect user inputs
user_inputs = []
for feature in selected_features:
    value = st.number_input(f"Enter value for {feature}:", min_value=0.0, step=0.1)
    user_inputs.append(value)

# Convert user inputs into a numpy array
input_array = np.array([user_inputs])

# Add prediction functionality
if st.button("Predict"):
    # Predict using the model
    prediction = model.predict(input_array)[0]
    prediction_proba = model.predict_proba(input_array)

    # Display results
    if prediction == 1:
        st.error("🚨 The person has a high probability of breast cancer. Please consult a doctor immediately.")
    else:
        st.success("✅ The person is predicted to be healthy.")

    # Display prediction probabilities
    st.write("### Prediction Probabilities:")
    st.write(f"- Healthy: {prediction_proba[0][0]:.2f}")
    st.write(f"- Sick: {prediction_proba[0][1]:.2f}")
