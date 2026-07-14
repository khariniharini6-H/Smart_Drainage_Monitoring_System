import streamlit as st
import pandas as pd

# Page Title
st.title("📊 Smart Drainage Dashboard")

st.write("### Live Drainage Monitoring Overview")

# Load Dataset
df = pd.read_csv("drainage_data.csv")

# Calculate Summary
total = len(df)
safe = len(df[df["Risk"] == "Safe"])
medium = len(df[df["Risk"] == "Medium"])
high = len(df[df["Risk"] == "High"])

# Display Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Drains", total)
col2.metric("Safe", safe)
col3.metric("Medium Risk", medium)
col4.metric("High Risk", high)

st.divider()

# Display Table
st.subheader("Drainage Monitoring Data")

st.dataframe(df, use_container_width=True)
