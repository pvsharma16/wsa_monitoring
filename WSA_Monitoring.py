import streamlit as st
import pandas as pd

st.title("📁 CSV from OneDrive")

# Replace with your actual download link
onedrive_url = "https://onedrive.live.com/download.aspx?resid=ABCDEF123456!789"

try:
    df = pd.read_csv(onedrive_url)
    st.success("CSV loaded from OneDrive!")
    st.dataframe(df)
except Exception as e:
    st.error(f"Failed to load CSV: {e}")
