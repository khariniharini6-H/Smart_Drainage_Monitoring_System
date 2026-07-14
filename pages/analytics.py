import streamlit as st
import pandas as pd

st.title("📈 Smart Drainage Analytics")

st.write("Visual analysis of the drainage monitoring data.")

# Load Dataset
df = pd.read_csv("drainage_data.csv")

# ----------------------------
# Risk Distribution
# ----------------------------
st.subheader("Risk Distribution")

risk_counts = df["Risk"].value_counts()

st.bar_chart(risk_counts)

# ----------------------------
# Water Level
# ----------------------------
st.subheader("💧 Water Level by Area")

water = df.set_index("Area")["Water_Level"]
st.bar_chart(water)

# ----------------------------
# Garbage Level
# ----------------------------
st.subheader("🗑 Garbage Level by Area")

garbage = df.set_index("Area")["Garbage_Level"]
st.bar_chart(garbage)
# ----------------------------
# Rainfall
# ----------------------------
st.subheader("🌧 Rainfall by Area")

rain = df.set_index("Area")["Rainfall"]
st.line_chart(rain)

# ----------------------------
# Flow Rate
# ----------------------------
st.subheader("💦 Flow_Rate by Area")

flow = df.set_index("Area")["Flow_Rate"]
st.line_chart(flow)
