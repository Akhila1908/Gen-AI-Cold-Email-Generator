# streamlit_app.py - Entry point for Streamlit Cloud
import sys
import os
from pathlib import Path

# Add the app directory to Python path
sys.path.append(os.path.join(Path(__file__).parent, "app"))

# Import and run the main app
from app.main import main as run_app

if __name__ == "__main__":
    run_app()
