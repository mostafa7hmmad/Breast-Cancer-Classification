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
def render_animation():
    animation_code = """
    <div style="display:flex;justify-content:center;align-items:center;margin-bottom:20px;">
        <div style="width:100px;height:100px;border-radius:50%;background-color:#ff5722;animation:bounce 2s infinite;"></div>
        <style>
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-20px); }
            }
        </style>
    </div>
    """
    st.components.v1.html(animation_code, height=200)

st.title("Breast Cancer Prediction App")
render_animation()
st.write("Enter the feature values below to determine the health status:")

# Collect user inputs
user_inputs = []
with st.form(key="feature_input_form"):
    for feature in selected_features:
        value = st.number_input(f"Enter value for {feature}:", min_value=0.0, step=0.1)
        user_inputs.append(value)

    submit_button = st.form_submit_button(label="Predict")

# Convert user inputs into a numpy array
if submit_button:
    input_array = np.array([user_inputs])

    # Add prediction functionality
    try:
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
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
