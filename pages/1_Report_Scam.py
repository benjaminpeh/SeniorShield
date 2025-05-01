# pages/1_Report_Scam.py
import streamlit as st

st.markdown("<h2 style='font-size: 40px;'>📢 Report a Scam</h2>", unsafe_allow_html=True)
st.markdown("Please fill in the form below to describe the scam you encountered. All information will be kept confidential.")

with st.form("report_form"):
    name = st.text_input("Your Name (optional)", placeholder="e.g. Mr Lim")
    scam_type = st.selectbox("Type of Scam", [
        "Phone Call Scam", "SMS/WhatsApp Scam", "Email Scam",
        "Impersonation", "Online Shopping Scam", "Others"
    ])
    description = st.text_area("Describe what happened in your own words", height=200)
    contact = st.text_input("Your Contact (optional)", placeholder="e.g. 91234567")
    submitted = st.form_submit_button("Submit Report")

if submitted:
    st.success("✅ Thank you for your report. We will follow up if necessary.")
    st.balloons()
