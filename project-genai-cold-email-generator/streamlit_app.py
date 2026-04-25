import sys
import os
from pathlib import Path

# Add the project root to path
sys.path.append(str(Path(__file__).parent))

from app.main import create_streamlit_app
from app.chains import Chain
from app.portfolio import Portfolio
from app.utils import clean_text
import streamlit as st
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Check API key
api_key = None
try:
    api_key = st.secrets.get("GROQ_API_KEY")
except:
    pass

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("""
    ## ⚠️ API Key Missing!
    
    Please add your GROQ_API_KEY to Streamlit Secrets:
    
    1. Go to **Settings → Secrets**
    2. Add: `GROQ_API_KEY = "your_key_here"`
    
    Or create a `.env` file locally.
    """)
    st.stop()

# Initialize and run
try:
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Job Application Assistant", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
except Exception as e:
    st.error(f"Failed to initialize: {str(e)}")
    st.info("Make sure all dependencies are installed: pip install -r requirements.txt")
