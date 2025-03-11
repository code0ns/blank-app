import streamlit as st
import pandas as pd
import random

# Function to predict startup success probability (Simplified for MVP)
def predict_startup_success(num_founders, funding_amount):
    success_prob = round((num_founders * 5 + (funding_amount / 1e6) * 10 + random.uniform(-5, 5)), 2)
    return success_prob

# Streamlit UI
st.title("🚀 Co-Founder Compatibility & Startup Success Predictor")
st.write("Enter details about your startup team to predict success probability.")

# User Inputs
num_founders = st.slider("👥 Number of Founders", 1, 10, 2)
funding_amount = st.number_input("💰 First Funding Amount ($)", min_value=0, value=1000000)

# Predict Success Probability
if st.button("🔮 Predict Success"):
    success_prob = predict_startup_success(num_founders, funding_amount)
    st.metric(label="📊 Predicted Success Probability", value=f"{success_prob}%")

st.write("🔹 **How does this work?**")
st.write("This MVP estimates startup success based on the number of co-founders and initial funding.")
st.write("📌 Future updates will include more factors like industry, investor data, and team chemistry.")