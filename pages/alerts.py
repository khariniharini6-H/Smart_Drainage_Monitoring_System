import streamlit as st
import pandas as pd

st.title("🚨 Smart Drainage Alert System")

# Load data
df = pd.read_csv("drainage_data.csv")

st.write("### Current Alerts")

high_risk = df[df["Risk"] == "High"]

if len(high_risk) == 0:
    st.success("✅ No High Risk Areas Found")
else:
    for index, row in high_risk.iterrows():
        st.error(
            f"🚨 ALERT: {row['Area']} is at HIGH RISK!\n\n"
            f"Water Level: {row['Water_Level']}\n"
            f"Garbage Level: {row['Garbage_Level']}\n"
            f"Rainfall: {row['Rainfall']}\n"
            f"Flow Rate: {row['Flow_Rate']}"
        )

st.divider()

st.write("### Full Drainage Status")
st.dataframe(df)
