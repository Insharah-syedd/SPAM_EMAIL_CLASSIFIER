import streamlit as st
import joblib
import time  # <--- Error se bachne ke liye ye lazmi hai

# 1. Page Config
st.set_page_config(page_title="Email Detector Pro", page_icon="🛡️", layout="wide")

# 2. Final Ultra-Massive UI Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Heading Section */
    .hero-heading {
        text-align: center;
        font-size: 90px !important;
        font-weight: 800;
        background: linear-gradient(to bottom, #ffffff 30%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 40px;
    }

    /* Input Area - Huge Font */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        padding: 40px !important;
        font-size: 32px !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        backdrop-filter: blur(15px);
    }

    /* Button Centering & Massive Size */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        padding: 35px 100px !important;
        border-radius: 20px !important;
        font-size: 45px !important;
        font-weight: 800 !important;
        min-width: 600px;
        text-transform: uppercase;
        letter-spacing: 5px;
        box-shadow: 0 0 50px rgba(59, 130, 246, 0.5);
        border: none !important;
    }

    /* Result Cards */
    .res-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(25px);
        border-radius: 45px;
        padding: 80px 30px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.08);
        min-height: 500px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .percentage-text {
        font-size: 130px !important;
        font-weight: 800;
        margin: 5px 0;
    }

    .description-text {
        color: #94a3b8 !important; 
        font-size: 24px !important;
        font-weight: 600 !important;
        margin-top: 15px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .label-text {
        font-size: 28px !important;
        font-weight: 700;
        letter-spacing: 4px;
        color: #ffffff;
    }

    .glow-red { text-shadow: 0 0 40px rgba(239, 68, 68, 0.6); color: #ef4444 !important; }
    .glow-green { text-shadow: 0 0 40px rgba(16, 185, 129, 0.6); color: #10b981 !important; }

    /* Hide Streamlit Branding */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Model Loading
@st.cache_resource
def load_assets():
    try:
        m = joblib.load('models/spam_model.pkl')
        v = joblib.load('models/tfidf_vectorizer.pkl')
        return m, v
    except: return None, None

model, tfidf = load_assets()

# 4. Building UI
st.markdown('<h1 class="hero-heading">EMAIL DETECTOR</h1>', unsafe_allow_html=True)

_, main_col, _ = st.columns([1, 6, 1])
with main_col:
    email_content = st.text_area("", placeholder=" EMAIL CONTENT...", height=250)
    scan_clicked = st.button("RUN ANALYSIS")

# 5. Result Display
if scan_clicked:
    if not email_content:
        st.warning("⚠️ Please enter some text to analyze!")
    elif model and tfidf:
        # --- SPINNER START ---
        with st.spinner('🧬 Neural Engine Analyzing Patterns...'):
            time.sleep(1.5)  # Professional delay
        
        # ML Logic
        vec = tfidf.transform([email_content])
        res = model.predict(vec)[0]
        probs = model.predict_proba(vec)[0]
        
        cls = list(model.classes_)
        s_idx = cls.index('spam') if 'spam' in cls else 1
        h_idx = 0 if s_idx == 1 else 1
        
        spam_p, ham_p = probs[s_idx] * 100, probs[h_idx] * 100

        # Output Cards
        st.markdown("<br><br>", unsafe_allow_html=True)
        r_col1, r_col2 = st.columns(2, gap="large")
        
        with r_col1:
            st.markdown(f"""
                <div class="res-card">
                    <div class="label-text">THREAT LEVEL</div>
                    <div class="percentage-text glow-red">{spam_p:.1f}%</div>
                    <div class="description-text">Malicious Risk Probability</div>
                </div>
            """, unsafe_allow_html=True)
            
        with r_col2:
            st.markdown(f"""
                <div class="res-card">
                    <div class="label-text">TRUST SCORE</div>
                    <div class="percentage-text glow-green">{ham_p:.1f}%</div>
                    <div class="description-text">Secure Integrity Verified</div>
                </div>
            """, unsafe_allow_html=True)
        
        # Result Status Bar
        st.markdown("<br>", unsafe_allow_html=True)
        _, msg_col, _ = st.columns([1, 8, 1])
        with msg_col:
            if res == 'spam':
                st.markdown(f'<div style="background: rgba(239, 68, 68, 0.15); color: #ef4444; padding: 25px; border-radius: 15px; border: 2px solid #ef4444; font-size: 28px; font-weight: 700; text-align: center;">🚨 THREAT DETECTED: This message shows strong spam patterns.</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background: rgba(16, 185, 129, 0.15); color: #10b981; padding: 25px; border-radius: 15px; border: 2px solid #10b981; font-size: 28px; font-weight: 700; text-align: center;">✅ SCAN PASSED: This email is verified as safe.</div>', unsafe_allow_html=True)
    else:
        st.error("❌ System Offline: Model files missing in 'models/' folder.")
        