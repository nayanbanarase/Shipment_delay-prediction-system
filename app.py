import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("shipment.csv")

# Input columns
X = df[['Distance', 'Weight', 'Cost']]

# Output column
y = df['Delayed']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Title
st.title("Shipment Prediction System")

# Inputs
distance = st.number_input("Enter Distance")
weight = st.number_input("Enter Weight")
cost = st.number_input("Enter Cost")

# Predict button
if st.button("Predict"):

    result = model.predict([[distance, weight, cost]])

    if result[0] == 1:
        st.error("Shipment Delayed")

    else:
        st.success("Shipment On Time")
