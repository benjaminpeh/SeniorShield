# pages/2_Scam_Quiz.py
import streamlit as st

st.markdown("<h2 style='font-size: 40px;'>🧠 Scam Detection Quiz</h2>", unsafe_allow_html=True)
st.write("Test your ability to spot common scam tactics.")

score = 0

# Question 1
q1 = st.radio("1️⃣ You receive a call saying you won a lucky draw, but need to pay $100 to claim it. What do you do?",
              ["Pay quickly to not miss out", "Ignore and hang up", "Give IC number first then decide"])
if q1 == "Ignore and hang up":
    score += 1

# Question 2
q2 = st.radio("2️⃣ You get an SMS from a 'bank' asking you to log in via a link. What should you do?",
              ["Click and check your account", "Call the bank via official hotline", "Reply asking who it is"])
if q2 == "Call the bank via official hotline":
    score += 1

# Question 3
q3 = st.radio("3️⃣ A stranger on Facebook asks for help transferring money. What’s your response?",
              ["Ask for details", "Block and report", "Offer to help if it’s urgent"])
if q3 == "Block and report":
    score += 1

# Results
if st.button("Check My Score"):
    st.success(f"✅ You got {score}/3 correct.")
    if score == 3:
        st.balloons()
        st.info("Excellent scam awareness! 💪")
    elif score == 2:
        st.info("Good job — stay alert!")
    else:
        st.warning("Be careful — scams are getting trickier. Learn more on the Help page.")
