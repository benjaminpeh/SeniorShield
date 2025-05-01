import streamlit as st

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
    "\ud83d\udd0e Paste & Check for Scam Keywords"
])

# ----------------------------
# \ud83e\uddd0 Scam Quiz (Enhanced)
# ----------------------------
if choice == "\ud83e\uddd0 Scam Quiz":
    st.markdown("## \ud83e\uddd0 Scam Detection Quiz")
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

    if st.button("\u2705 Submit Answers"):
        st.markdown("---")
        st.success(f"\ud83c\udfaf You scored **{score} out of {total}**.")

        if score == total:
            st.balloons()
            st.info("\ud83c\udf89 Excellent! You're highly scam-aware.")
        elif score >= 3:
            st.info("\ud83d\udc4d Good job — just a few areas to watch.")
        else:
            st.warning("\u26a0\ufe0f You may be vulnerable to scams. Check the Help page to learn more.")

        if explanations:
            st.markdown("### \ud83d\udca1 Here's how to improve:")
            for explain in explanations:
                st.markdown(f"- {explain}")

# ----------------------------
# \ud83d\udcde Help & Contacts
# ----------------------------
elif choice == "\ud83d\udcde Help & Contacts":
    st.markdown("## \ud83d\udcde Scam Help & Contacts")
    st.markdown("Need help or want to report a scam? Here are official resources:")

    st.markdown("### \ud83d\udccc Singapore Scam Reporting Hotlines")
    st.markdown("""
    - ☎️ **Anti-Scam Helpline**: **1800-722-6688**
    - 🚨 **Police Emergency Hotline**: **999**
    - 🕵️‍♀️ **National Crime Prevention Council (NCPC)**: [scamalert.sg](https://www.scamalert.sg)
    - 📱 **ScamShield**: [scamshield.org.sg](https://www.scamshield.org.sg)
    """)

    st.markdown("### \u2705 Safety Tips for Seniors")
    st.markdown("""
    - ❌ Never give out your **OTP**, **NRIC**, or **passwords** to anyone.
    - ❌ Do not click on suspicious links in SMS, WhatsApp, or email.
    - ☎️ Always **verify calls** with official hotlines.
    - ✅ Use the **ScamShield app** to block scams.
    """)

    st.info("This app was designed with seniors in mind. Share it with your loved ones.")

# ----------------------------
# \ud83d\udcda Scam Awareness Courses
# ----------------------------
elif choice == "\ud83d\udcda Scam Awareness Courses":
    st.markdown("## \ud83d\udcda Scam Awareness Courses for Seniors in Singapore")
    st.markdown("Stay up to date with free scam prevention programmes offered across Singapore:")

    st.markdown("### \ud83d\udca1 Courses & Workshops")
    st.markdown("""
    - **IMDA Digital Skills for Life (Seniors Go Digital)**  
      [https://www.imda.gov.sg/programme-listing/Seniors-Go-Digital](https://www.imda.gov.sg/programme-listing/Seniors-Go-Digital)  
      _Learn how to spot scams, use mobile apps safely, and browse securely._

    - **Cyber Security Agency (CSA) Scam Awareness Roadshows**  
      Watch for their pop-up events at community centres and libraries.

    - **People’s Association (PA) Digital Literacy Courses**  
      Visit your nearest Community Centre for basic scam awareness talks and digital skills training.
    """)

    st.markdown("\ud83d\udcac Want help registering? Call the **Silver Infocomm Hotline** at **6377-3800**.")

# ----------------------------
# \ud83d\udd0e Paste & Check Text for Scam Keywords
# ----------------------------
elif choice == "\ud83d\udd0e Paste & Check for Scam Keywords":
    st.markdown("## \ud83d\udd0e Paste Message Text to Check for Scams")
    user_text = st.text_area("Paste your message here (e.g., from SMS, email, or chat)")

    if st.button("\ud83d\udd0e Analyze Message"):
        scam_keywords = ["prize", "otp", "urgent", "password", "click", "transfer", "verify", "win", "login", "bank"]
        found = [word for word in scam_keywords if word in user_text.lower()]

        if found:
            st.warning(f"\u26a0\ufe0f Suspicious words detected: {', '.join(found)}")
            st.info("Please verify this message with someone you trust before acting on it.")
        else:
            st.success("\u2705 No common scam keywords found. Stay alert and safe!")
