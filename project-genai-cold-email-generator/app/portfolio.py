import pandas as pd
from pathlib import Path
import streamlit as st

class Portfolio:
    def __init__(self, file_path=None):
        try:
            if file_path is None:
                # Get the directory where this file is located (app folder)
                current_dir = Path(__file__).parent
                file_path = current_dir / "resource" / "my_portfolio.csv"
            
            self.file_path = str(file_path)
            
            if not Path(self.file_path).exists():
                st.warning(f"Portfolio file not found at {self.file_path}")
                self.data = pd.DataFrame(columns=["Techstack", "Links"])
            else:
                self.data = pd.read_csv(self.file_path)
                print(f"Loaded {len(self.data)} portfolio entries from {self.file_path}")
        except Exception as e:
            st.error(f"Error loading portfolio: {str(e)}")
            self.data = pd.DataFrame(columns=["Techstack", "Links"])

    def load_portfolio(self):
        # Simple text matching - no ChromaDB needed
        pass

    def query_links(self, skills):
        """Simple keyword matching to find relevant portfolio links"""
        if not skills or self.data.empty:
            return []
        
        matched_links = []
        for _, row in self.data.iterrows():
            techstack = str(row["Techstack"]).lower()
            # Check if any skill matches the techstack
            for skill in skills:
                if skill.lower() in techstack:
                    matched_links.append(row["Links"])
                    if len(matched_links) >= 2:
                        return [{"links": ", ".join(matched_links)}]
                    break
        
        return [{"links": ", ".join(matched_links)}] if matched_links else []
