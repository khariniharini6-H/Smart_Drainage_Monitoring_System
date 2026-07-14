import streamlit as st
import pandas as pd
from datetime import datetime

# Load Dataset
df = pd.read_csv("drainage_data.csv")

st.title("📄 Smart Drainage Monitoring Report")

st.write("Professional Drainage Report")

# Current Date
st.write("### Report Generated On")
st.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.divider()

# Dashboard Summary
st.subheader("📊 Dashboard Summary")

total = len(df)
safe = len(df[df["Risk"] == "Safe"])
medium = len(df[df["Risk"] == "Medium"])
high = len(df[df["Risk"] == "High"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Drains", total)
col2.metric("Safe", safe)
col3.metric("Medium", medium)
col4.metric("High", high)

st.divider()

# High Risk Areas
st.subheader("🚨 High Risk Areas")

high_df = df[df["Risk"] == "High"]

if high_df.empty:
    st.success("No High Risk Areas")
else:
    st.dataframe(high_df)

st.divider()

# Complete Dataset
st.subheader("📋 Complete Drainage Report")

st.dataframe(df)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Report",
    data=csv,
    file_name="Drainage_Report.csv",
    mime="text/csv"
)
