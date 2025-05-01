# app.py
import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Header ---
st.markdown("<h1 style='font-size: 50px;'>🛡️ SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 28px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Intro Text ---
st.write("Welcome to **SeniorShield**, a simple and safe space to learn about scams and report suspicious activity. "
         "This platform is designed with elderly users in mind — using big fonts, clear steps, and easy navigation.")

# --- Navigation Choice ---
st.write("### What would you like to do today?")
choice = st.selectbox("Choose an option:", [
    "🧠 Learn to Detect Scams (Quiz)",
    "📢 Report a Scam",
    "📞 Scam Help & Contacts"
])

# --- Page Navigation ---
if choice == "🧠 Learn to Detect Scams (Quiz)":
    st.info("🚧 This feature will be available soon.")
elif choice == "📢 Report a Scam":
    st.info("🚧 This feature will be available soon.")
elif choice == "📞 Scam Help & Contacts":
    st.info("🚧 This feature will be available soon.")
