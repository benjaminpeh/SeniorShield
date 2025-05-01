import streamlit as st
import joblib

# --- Load Pre-trained Scam Classifier ---
model = joblib.load("scam_classifier.pkl")  # Ensure this file is in the same folder on Streamlit Cloud
vectorizer = joblib.load("vectorizer.pkl")  # Your TF-IDF vectorizer or similar

# --- Page Setup ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='font-size: 50px;'>SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 26px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Navigation Menu ---
choice = st.selectbox("What would you like to do?", [
    "\ud83e\uddd0 Scam Quiz",
    "\ud83d\udcde Help & Contacts",
    "\ud83d\udcda Scam Awareness Courses",
    "\ud83d\udd0e Paste Message to Check for Scam"
])

# --- Pages (Quiz, Help, Courses remain the same) ---
if choice == "\ud83e\uddd0 Scam Quiz":
    st.markdown("## \ud83e\uddd0 Scam Detection Quiz")
    st.write("[Your quiz content remains unchanged here...]")

elif choice == "\ud83d\udcde Help & Contacts":
    st.markdown("## \ud83d\udcde Scam Help & Contacts")
    st.write("[Help contact info remains unchanged here...]")

elif choice == "\ud83d\udcda Scam Awareness Courses":
    st.markdown("## \ud83d\udcda Scam Awareness Courses")
    st.write("[Course listing remains unchanged here...]")

# --- ML Text Classifier for Scam Detection ---
elif choice == "\ud83d\udd0e Paste Message to Check for Scam":
    st.markdown("## \ud83d\udd0e Paste and Scan for Scam Risk")
    st.write("Paste a suspicious message (e.g. from SMS or email) to let our model determine scam risk.")

    user_input = st.text_area("Enter the message text here:", height=200)

    if st.button("\ud83d\udd0e Analyze Message") and user_input:
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        prob = model.predict_proba(X_input)[0]
        scam_score = round(prob[1]*100, 2)

        if prediction == 1:
            st.error(f"⚠️ This message is likely a **SCAM**. Risk score: {scam_score}%")
            st.info("Do not reply or click any links. Verify with a trusted source.")
        else:
            st.success(f"✅ This message appears safe. Scam probability: {scam_score}%")
            st.info("Stay cautious and always verify unusual requests.")
