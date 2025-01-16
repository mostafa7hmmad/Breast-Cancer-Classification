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
st.title("Health Prediction App")
st.write("Enter the feature values to predict whether the person is sick or not.")

# User input for each feature
user_inputs = []
for feature in selected_features:
    value = st.number_input(f"Enter value for {feature}", value=0.0)
    user_inputs.append(value)

# Convert user inputs into a numpy array
input_array = np.array([user_inputs])

# Prediction button
if st.button("Predict"):
    # Make prediction
    prediction = model.predict(input_array)
    prediction_proba = model.predict_proba(input_array)

    # Display results
    if prediction[0] == 1:
        st.error("The person is predicted to be SICK 🚨")
    else:
        st.success("The person is predicted to be HEALTHY ✅")

    # Display probabilities
    st.write(f"Prediction Probabilities: Healthy: {prediction_proba[0][0]:.2f}, Sick: {prediction_proba[0][1]:.2f}")
