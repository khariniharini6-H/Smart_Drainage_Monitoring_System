import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("drainage_data.csv")

# Convert Risk into numbers
risk_map = {
    "Safe": 0,
    "Medium": 1,
    "High": 2
}

df["Risk"] = df["Risk"].map(risk_map)

# Features
X = df[["Water_Level", "Garbage_Level", "Rainfall", "Flow_Rate"]]

# Target
y = df["Risk"]

# Create Model
model = RandomForestClassifier(random_state=42)

# Train Model
model.fit(X, y)

# Save Model
joblib.dump(model, "models/drainage_model.pkl")


print("✅ Model Trained Successfully!")
