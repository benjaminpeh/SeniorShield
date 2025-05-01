import streamlit as st

# --- App Setup ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Hide Sidebar ---
hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='font-size: 50px;'>🛡️ SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 26px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Navigation ---
choice = st.selectbox("What would you like to do?", [
    "👋 Home",
    "📢 Report a Scam",
    "🧠 Scam Quiz",
    "📞 Help & Contacts"
])

# --- Home Page ---
if choice == "👋 Home":
    st.write("Welcome to **SeniorShield**, a simple and safe platform to help elderly users detect, understand, and report scams.")
    st.write("This site is designed with accessibility in mind: large fonts, minimal distractions, and clear navigation.")

# --- Scam Report Page ---
elif choice == "📢 Report a Scam":
    st.markdown("## 📢 Report a Scam")
    st.markdown("Fill in this form to describe the scam you encountered:")

    with st.form("report_form"):
        name = st.text_input("Your Name (optional)")
        scam_type = st.selectbox("Type of Scam", [
            "Phone Call", "WhatsApp/SMS", "Email", "Impersonation", "Online Purchase", "Other"
        ])
        description = st.text_area("What happened?", height=200)
        contact = st.text_input("Your Contact (optional)")
        submitted = st.form_submit_button("Submit Report")

    if submitted:
        st.success("✅ Thank you. Your report has been received.")
        st.balloons()

# --- Scam Quiz Page ---
elif choice == "🧠 Scam Quiz":
    st.markdown("## 🧠 Scam Detection Quiz")
    st.write("Test your scam awareness with a short quiz.")

    score = 0

    q1 = st.radio("1. You get a call saying you've won a lucky draw but must pay $100 to claim it. What do you do?",
                  ["Pay quickly", "Hang up immediately", "Ask for their NRIC"])
    if q1 == "Hang up immediately":
        score += 1

    q2 = st.radio("2. You receive an SMS with a suspicious link from 'your bank'. What should you do?",
                  ["Click and log in", "Call the bank's hotline", "Reply to ask for info"])
    if q2 == "Call the bank's hotline":
        score += 1

    q3 = st.radio("3. Someone on Facebook says they need your help to transfer money. You should:",
                  ["Ask what it's for", "Ignore or block", "Offer help"])
    if q3 == "Ignore or block":
        score += 1

    if st.button("Submit Answers"):
        st.success(f"You got {score}/3 correct.")
        if score == 3:
            st.info("🎉 Great job! You're scam smart.")
            st.balloons()
        elif score == 2:
            st.info("👍 Not bad — keep learning.")
        else:
            st.warning("😬 Be careful — scammers are tricky. Learn more on the Help page.")

# --- Help & Contacts Page ---
elif choice == "📞 Help & Contacts":
    st.markdown("## 📞 Scam Help & Contacts")
    st.markdown("""
    ### 📌 Hotlines
    - Anti-Scam Helpline (Singapore): **1800-722-6688**
    - Police: **999**
    - ScamShield: [scamshield.org.sg](https://www.scamshield.org.sg)

    ### ✅ Safety Tips
    - Never give out OTPs, passwords, or NRICs.
    - Don't click unknown links.
    - Verify all calls with official sources.
    """)

    st.info("This app was designed for seniors. Share it with those who may need help spotting scams.")
