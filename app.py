import streamlit as st
import pytesseract
from PIL import Image
import io

# --- Page Setup ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='font-size: 50px;'>\ud83d\udee1\ufe0f SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 26px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Navigation Menu ---
choice = st.selectbox("What would you like to do?", [
    "\ud83e\uddd0 Scam Quiz",
    "\ud83d\udcde Help & Contacts",
    "\ud83d\udcda Scam Awareness Courses",
    "\ud83d\udcf7 Scan a Screenshot for Scams"
])

# --- Scam Quiz (same as before) ---
if choice == "\ud83e\uddd0 Scam Quiz":
    # [Insert existing Scam Quiz block here, unchanged]
    st.write("[Scam Quiz content remains unchanged here...]")

# --- Help & Contacts (same as before) ---
elif choice == "\ud83d\udcde Help & Contacts":
    # [Insert existing Help & Contacts block here, unchanged]
    st.write("[Help & Contacts content remains unchanged here...]")

# --- Scam Awareness Courses (same as before) ---
elif choice == "\ud83d\udcda Scam Awareness Courses":
    # [Insert existing Scam Awareness Courses block here, unchanged]
    st.write("[Scam Awareness Courses content remains unchanged here...]")

# --- NEW: Upload Screenshot to Detect Scam ---
elif choice == "\ud83d\udcf7 Scan a Screenshot for Scams":
    st.markdown("## \ud83d\udcf7 Upload Screenshot or Email Screenshot")
    st.write("Let us help you detect if the message might be a scam.")

    uploaded_file = st.file_uploader("Upload a screenshot (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Screenshot", use_column_width=True)

        with st.spinner("Scanning for suspicious words..."):
            text = pytesseract.image_to_string(image)

            scam_keywords = ["prize", "otp", "password", "urgent", "click", "login", "bank", "transfer", "money", "win", "payment", "verify", "account"]
            found_keywords = [kw for kw in scam_keywords if kw.lower() in text.lower()]

            st.markdown("### 🔍 Detected Text:")
            st.text(text.strip())

            if found_keywords:
                st.warning(f"⚠️ This message contains words that are often used in scams: {', '.join(found_keywords)}")
                st.info("Please verify the message source or contact someone you trust before taking any action.")
            else:
                st.success("✅ No major scam-related keywords detected. Stay alert and safe!")
