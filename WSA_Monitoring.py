import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title("📥 Load CSV from SharePoint")

# Replace with your actual shared URL
sharepoint_url = "https://whitespacefund-my.sharepoint.com/:x:/g/personal/fanar_iskif_whitespacealpha_com/Eay2NBFK6RNKmKAKni25yqUBPLH4TeVhlzOgJ1uVreHpZA?e=lHJKp0"

try:
    # Simulate browser-like download
    response = requests.get(sharepoint_url)
    if response.status_code == 200:
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)
        st.success("Loaded CSV from SharePoint!")
        st.dataframe(df)
    else:
        st.error(f"Failed to fetch file: HTTP {response.status_code}")
except Exception as e:
    st.error(f"Error: {e}")
