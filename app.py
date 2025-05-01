# app.py
import streamlit as st

# --- App Config ---
st.set_page_config(page_title="SeniorShield", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='font-size: 50px;'>\ud83d\udee1\ufe0f SeniorShield</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 26px;'>Protecting seniors from scams with awareness and action</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Language Selection ---
lang = st.selectbox("\ud83c\udf10 Choose Language / 选择语言 / Pilih Bahasa / மொழியைத் தேர்ந்தெடுக்கவும்", 
                    options=["English", "中文", "Malay", "Tamil"])

# --- Navigation ---
page = st.selectbox("What would you like to do?", [
    "\ud83e\uddd0 Scam Quiz",
    "\ud83d\udcde Help & Contacts",
    "\ud83d\udcda Scam Awareness Courses"
])

# === Translations for All Sections ===
labels = {
    "English": {
        "help": "## \ud83d\udcde Scam Help & Contacts\n### \ud83d\udccc Hotlines\n- Anti-Scam Helpline (Singapore): **1800-722-6688**\n- Police: **999**\n- ScamAlert: [scamalert.sg](https://www.scamalert.sg)\n- ScamShield: [scamshield.org.sg](https://www.scamshield.org.sg)\n\n### \u2705 Safety Tips\n- Never give out OTPs, passwords, or NRICs.\n- Don’t click unknown links.\n- Always verify calls with official sources.",
        "courses": "## \ud83d\udcda Scam Awareness Courses\n### \ud83d\udca1 Free Programmes in Singapore\n- **IMDA Seniors Go Digital**: Scam spotting & safe digital skills\n- **CSA Scam Roadshows** at CCs & libraries\n- **PA Digital Literacy Courses** in your neighbourhood\n\nFor help registering, call **6377-3800**."
    },
    "中文": {
        "help": "## \ud83d\udcde 防骗帮助与联系方式\n### \ud83d\udccc 热线电话\n- 防骗热线（新加坡）：**1800-722-6688**\n- 警察：**999**\n- 防骗网站: [scamalert.sg](https://www.scamalert.sg)\n- ScamShield 应用: [scamshield.org.sg](https://www.scamshield.org.sg)\n\n### \u2705 安全提示\n- 切勿泄露OTP、密码或身份证号码。\n- 不要点击陌生链接。\n- 请通过官方渠道验证来电。",
        "courses": "## \ud83d\udcda 防骗课程\n### \ud83d\udca1 新加坡免费课程\n- **IMDA数码乐龄计划**：识别诈骗与数码安全\n- **CSA巡回讲座**：社区中心与图书馆举行\n- **人民协会课程**：本地居民可参加\n\n报名请拨打：**6377-3800**"
    },
    "Malay": {
        "help": "## \ud83d\udcde Bantuan & Nombor Penting\n### \ud83d\udccc Talian\n- Talian Anti-Scam: **1800-722-6688**\n- Polis: **999**\n- ScamAlert: [scamalert.sg](https://www.scamalert.sg)\n- ScamShield: [scamshield.org.sg](https://www.scamshield.org.sg)\n\n### \u2705 Petua Keselamatan\n- Jangan kongsi OTP, kata laluan, atau NRIC.\n- Jangan klik pautan yang tidak dikenali.\n- Semak panggilan melalui nombor rasmi.",
        "courses": "## \ud83d\udcda Kursus Kesedaran Scam\n### \ud83d\udca1 Program Percuma\n- **IMDA Seniors Go Digital**\n- **CSA Kempen Scam**\n- **Kursus Digital PA** di pusat komuniti\n\nDaftar melalui hotline: **6377-3800**"
    },
    "Tamil": {
        "help": "## \ud83d\udcde மோசடி உதவி மற்றும் தொலைபேசி எண்கள்\n### \ud83d\udccc ஹாட்லைன்கள்\n- மோசடி உதவி: **1800-722-6688**\n- காவல் துறைக்கு: **999**\n- ScamAlert: [scamalert.sg](https://www.scamalert.sg)\n- ScamShield: [scamshield.org.sg](https://www.scamshield.org.sg)\n\n### \u2705 பாதுகாப்பு அறிவுரை\n- OTP, கடவுச்சொல், NRIC பகிர வேண்டாம்.\n- தெரியாத இணைப்புகளை கிளிக் செய்யவேண்டாம்.\n- அதிகாரபூர்வ எண்ணை உறுதிப்படுத்தவும்.",
        "courses": "## \ud83d\udcda மோசடி விழிப்புணர்வு வகுப்புகள்\n### \ud83d\udca1 இலவச திட்டங்கள்\n- **IMDA Seniors Go Digital**\n- **CSA சாலை நிகழ்வுகள்**\n- **PA டிஜிட்டல் கல்வி வகுப்புகள்**\n\nபதிவு செய்ய: **6377-3800**"
    }
}

# === PAGE: QUIZ ===
if page == "\ud83e\uddd0 Scam Quiz":
    st.markdown("## \ud83e\uddd0 Scam Detection Quiz")
    st.write("Test your scam awareness in your selected language:")

    # Include quiz logic from previous cell here (you already have it)
    # Use questions[lang] to get localized quiz questions (see previous assistant message)
    # Paste full quiz block here if needed

# === PAGE: HELP & CONTACTS ===
elif page == "\ud83d\udcde Help & Contacts":
    st.markdown(labels[lang]["help"], unsafe_allow_html=True)

# === PAGE: COURSES ===
elif page == "\ud83d\udcda Scam Awareness Courses":
    st.markdown(labels[lang]["courses"], unsafe_allow_html=True)
