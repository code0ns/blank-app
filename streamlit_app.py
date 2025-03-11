import streamlit as st
import pandas as pd
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    return pickle.load(open("startup_success_model.pkl", "rb"))

model = load_model()

# Function to predict startup success probability
def predict_startup_success(num_founders, funding_amount):
    input_data = pd.DataFrame([[num_founders, funding_amount]], columns=['Num_Founders', 'First_Funding_Amount'])
    prediction = model.predict_proba(input_data)[0][1]  # Probability of success
    return round(prediction * 100, 2)  # Convert to percentage

# ---- Streamlit Web App ----
st.set_page_config(page_title="Startup Success Predictor", page_icon="🚀", layout="centered")

st.title("🚀 Co-Founder Compatibility & Startup Success Predictor")
st.subheader("Enter your startup team details to predict success probability!")

# User Inputs
num_founders = st.slider("👥 Number of Founders", 1, 10, 2)
funding_amount = st.number_input("💰 First Funding Amount ($)", min_value=0, value=1000000, step=50000)

# Predict Success Probability
if st.button("🔮 Predict Success"):
    success_prob = predict_startup_success(num_founders, funding_amount)
    st.metric(label="📊 Predicted Success Probability", value=f"{success_prob}%")

st.divider()
st.write("🔹 **How does this work?**")
st.write("This MVP estimates startup success based on:")
st.write("✅ **Number of co-founders** - More diverse teams tend to succeed.")
st.write("✅ **Initial funding amount** - Startups with more capital have higher survival rates.")
st.write("📌 Future updates will include **industry factors, investor backing, and team chemistry analysis!**")