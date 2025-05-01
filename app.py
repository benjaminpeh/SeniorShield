import streamlit as st
from PIL import Image
import pytesseract

# --- Page Setup ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='font-size: 50px;'>🛡️ SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 26px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Navigation Menu ---
choice = st.selectbox("What would you like to do?", [
    "🧠 Scam Quiz",
    "📞 Help & Contacts",
    "📚 Scam Awareness Courses",
    "🖼️ Scam Image Detector"
])

# ----------------------------
# 🧠 Scam Quiz
# ----------------------------
if choice == "🧠 Scam Quiz":
    st.markdown("## 🧠 Scam Detection Quiz")
    st.write("Answer the following questions to test your scam awareness:")
    st.markdown("---")

    score = 0
    total = 5
    explanations = []

    q1 = st.radio("**1.** You get a call saying you've won a lucky draw but must pay $100 to claim it. What do you do?",
                  ["Pay quickly", "Hang up immediately", "Ask for their NRIC"], index=None)
    if q1:
        if q1 == "Hang up immediately":
            score += 1
        else:
            explanations.append("Q1: Scammers often ask for payment to claim fake prizes. Hang up immediately.")

    q2 = st.radio("**2.** You receive an SMS with a suspicious link from 'your bank'. What should you do?",
                  ["Click and log in", "Call the bank's hotline", "Reply to ask for info"], index=None)
    if q2:
        if q2 == "Call the bank's hotline":
            score += 1
        else:
            explanations.append("Q2: Never click links from unknown messages. Always call the bank directly.")

    q3 = st.radio("**3.** Someone on Facebook says they need your help to transfer money. You should:",
                  ["Ask what it's for", "Ignore or block", "Offer help"], index=None)
    if q3:
        if q3 == "Ignore or block":
            score += 1
        else:
            explanations.append("Q3: Scammers often use social media. Always ignore or block unknown requests.")

    q4 = st.radio("**4.** A message says your Singpass is locked and you must click a link to unlock. What do you do?",
                  ["Click and unlock it", "Log in manually to check", "Ignore and report it"], index=None)
    if q4:
        if q4 == "Ignore and report it":
            score += 1
        else:
            explanations.append("Q4: Official sites like Singpass never send links via SMS. Ignore and report them.")

    q5 = st.radio("**5.** You receive a call from someone claiming to be the police, asking for your IC and bank details. What should you do?",
                  ["Provide the info slowly", "Ask for their badge number", "Hang up and call the real police"], index=None)
    if q5:
        if q5 == "Hang up and call the real police":
            score += 1
        else:
            explanations.append("Q5: Real police will never ask for your IC/bank details over the phone.")

    if st.button("✅ Submit Answers"):
        st.markdown("---")
        st.success(f"🎯 You scored **{score} out of {total}**.")

        if score == total:
            st.balloons()
            st.info("🎉 Excellent! You're highly scam-aware.")
        elif score >= 3:
            st.info("👍 Good job — just a few areas to watch.")
        else:
            st.warning("⚠️ You may be vulnerable to scams. Check the Help page to learn more.")

        if explanations:
            st.markdown("### 💡 Here's how to improve:")
            for explain in explanations:
                st.markdown(f"- {explain}")

# ----------------------------
# 📞 Help & Contacts
# ----------------------------
elif choice == "📞 Help & Contacts":
    st.markdown("## 📞 Scam Help & Contacts")
    st.markdown("Need help or want to report a scam? Here are official resources:")

    st.markdown("### 📌 Singapore Scam Reporting Hotlines")
    st.markdown("""
    - ☎️ **Anti-Scam Helpline**: **1800-722-6688**
    - 🚨 **Police Emergency Hotline**: **999**
    - 🕵️‍♀️ **National Crime Prevention Council (NCPC)**: [scamalert.sg](https://www.scamalert.sg)
    - 📱 **ScamShield**: [scamshield.org.sg](https://www.scamshield.org.sg)
    """)

    st.markdown("### ✅ Safety Tips for Seniors")
    st.markdown("""
    - ❌ Never give out your **OTP**, **NRIC**, or **passwords** to anyone.
    - ❌ Do not click on suspicious links in SMS, WhatsApp, or email.
    - ☎️ Always **verify calls** with official hotlines.
    - ✅ Use the **ScamShield app** to block scams.
    """)

    st.info("This app was designed with seniors in mind. Share it with your loved ones.")

# ----------------------------
# 📚 Scam Awareness Courses
# ----------------------------
elif choice == "📚 Scam Awareness Courses":
    st.markdown("## 📚 Scam Awareness Courses for Seniors in Singapore")
    st.markdown("Stay up to date with free scam prevention programmes offered across Singapore:")

    st.markdown("### 💡 Courses & Workshops")
    st.markdown("""
    - **IMDA Digital Skills for Life (Seniors Go Digital)**  
      [https://www.imda.gov.sg/programme-listing/Seniors-Go-Digital](https://www.imda.gov.sg/programme-listing/Seniors-Go-Digital)  
      _Learn how to spot scams, use mobile apps safely, and browse securely._

    - **Cyber Security Agency (CSA) Scam Awareness Roadshows**  
      Watch for their pop-up events at community centres and libraries.

    - **People’s Association (PA) Digital Literacy Courses**  
      Visit your nearest Community Centre for basic scam awareness talks and digital skills training.
    """)

    st.markdown("💬 Want help registering? Call the **Silver Infocomm Hotline** at **6377-3800**.")

# ----------------------------
# 🖼️ Scam Image Detector
# ----------------------------
elif choice == "🖼️ Scam Image Detector":
    st.markdown("## 🖼️ Scam Image Detector")
    st.write("Upload a screenshot of a suspicious message or email. Our AI will help check if it's a scam.")

    uploaded_file = st.file_uploader("Upload your screenshot (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.markdown("### 🔍 Extracting text from image...")
        extracted_text = pytesseract.image_to_string(image)

        if extracted_text.strip():
            st.code(extracted_text, language="text")

            scam_keywords = [
                "bank account", "otp", "login here", "click link", "urgent",
                "singpass", "verify", "reward", "lucky draw", "password", "transfer"
            ]

            scam_count = sum(1 for kw in scam_keywords if kw.lower() in extracted_text.lower())

            if scam_count >= 2:
                st.error("🚨 Warning: Multiple scam-related keywords found. This may be a scam.")
            elif scam_count == 1:
                st.warning("⚠️ Caution: 1 suspicious keyword found. Be careful.")
            else:
                st.success("✅ No obvious scam terms found. Still, stay alert.")
        else:
            st.warning("❗ No readable text found. Try uploading a clearer screenshot.")
