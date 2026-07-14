import streamlit as st
import joblib
import pandas as pd
import os

# Load AI Model
model_path = os.path.join(os.path.dirname(
    __file__), "..", "drainage_model.pkl")
model = joblib.load(model_path)

st.title("🤖 AI Drainage Risk Prediction")

st.write("Enter the drainage details below.")

# User Inputs
water = st.slider("🌊 Water Level", 0, 100, 50)
garbage = st.slider("🗑️ Garbage Level", 0, 100, 50)
rainfall = st.slider("🌧️ Rainfall", 0, 100, 50)
flow = st.slider("💧 Flow Rate", 0, 100, 50)

# Display Prediction and Alert
if st.button("Predict Risk", key="predict_btn"):

    prediction = model.predict([[water, garbage, rainfall, flow]])

    if prediction[0] == 0:
        st.success("✅ Safe")
    elif prediction[0] == 1:
        st.warning("⚠️ Medium Risk")
    else:
        st.error("🚨 High Risk")
