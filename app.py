import streamlit as st

# --- Sidebar ---
st.sidebar.title("🧠 About This App")
st.sidebar.markdown("""
This **Fake News Detector** uses a **fixed dataset**  
to predict whether a news text is **Real or Fake** 📰  

### 💻 Tech Stack:
- Python & Streamlit  
- NLP (Text Processing)

👩‍💻 Developed by: *Sherley.G*
""")

# --- Page Setup ---
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# --- Background ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-photo/newspaper-background-concept_23-2151499628.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top:0; left:0; right:0; bottom:0;
    background: rgba(255,255,255,0.85);
}
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
[data-testid="stSidebar"] { background-color: #fafafa; }
h1, h2, h3 { color: #2c3e50; text-align: center; }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Button & Result Styles ---
button_style = """
<style>
div.stButton > button { background-color: #007BFF; color:white; border-radius:10px; padding:0.6em 1.2em; border:none; }
div.stButton > button:hover { background-color:#0056b3; transform: scale(1.03);}
.result-box { background-color:white; border-radius:12px; padding:1em; margin-top:1em; box-shadow:0 2px 8px rgba(0,0,0,0.1); font-size:1.1em; text-align:center;}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# --- App Title ---
st.title("📰 Fake News Detector")
st.subheader("Check whether a news article is Real or Fake")

# --- Fixed Dataset ---
fixed_labels = {
    "NASA successfully launches new satellite to study Mars": "REAL",
    "Celebrity found alive on Mars after NASA mission": "FAKE",
    "Government announces new education policy for rural areas": "REAL",
    "Scientists confirm chocolate cures all diseases": "FAKE",
    "WHO declares end of pandemic globally": "REAL"
}

# --- Text Box for Manual Input ---
news_text = st.text_area("Enter News Text:")

# --- Check Button ---
if st.button("Check"):
    news_input = news_text.strip()
    if news_input == "":
        st.warning("⚠️ Please enter some text to check.")
    elif news_input in fixed_labels:
        prediction = fixed_labels[news_input]
        if prediction == "REAL":
            st.markdown('<div class="result-box" style="color:green;">✅ This news looks REAL!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box" style="color:red;">❌ This news looks FAKE!</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ This news is not in the dataset. Cannot predict.")
