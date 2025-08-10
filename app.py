# app.py

import streamlit as st
from utils.translator import get_translator

# Configure app layout
st.set_page_config(
    page_title="Childhood Obesity Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize translator in session_state (only once)
if 'translator' not in st.session_state:
    st.session_state['translator'] = get_translator('en')  # default to English

# Language Selector UI
lang = st.selectbox("🌐 Select Language", ['English', 'Italiano', 'Ελληνικά', '中文'], key="language_select")

# Update session translator dynamically
if lang == 'English':
    st.session_state['translator'] = get_translator('en')
elif lang == 'Italiano':
    st.session_state['translator'] = get_translator('it')
elif lang == 'Ελληνικά':
    st.session_state['translator'] = get_translator('el')
elif lang == '中文':
    st.session_state['translator'] = get_translator('zh-cn')

# Display homepage intro
_ = st.session_state['translator'].translate
st.title(_("🏠 Welcome to the Childhood Obesity Risk Dashboard"))

st.markdown(_("""
This tool uses publicly available Australian health data to predict childhood obesity risk based on lifestyle and demographic factors.

Use the left sidebar to navigate:
- Explore data
- Run predictions
- View trends and fairness insights

**Note:** This is an educational prototype — no personal data is collected or stored.
"""))
