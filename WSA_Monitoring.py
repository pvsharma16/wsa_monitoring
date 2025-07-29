import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="CSV Hot Reload", layout="wide")
st.title("♻️ CSV Hot Reload Viewer (Streamlit Cloud Friendly)")

csv_path = "data/my_data.csv"

# Upload a new file (optional)
uploaded_file = st.file_uploader("Upload new CSV to overwrite", type="csv")
if uploaded_file:
    with open(csv_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("File uploaded and saved.")

# Show last mod time
def get_mod_time(path):
    return os.path.getmtime(path) if os.path.exists(path) else None

@st.cache_data(ttl=10)
def load_data(path, mod_time):
    return pd.read_csv(path)

if os.path.exists(csv_path):
    mod_time = get_mod_time(csv_path)
    df = load_data(csv_path, mod_time)
    st.success(f"Loaded from `{csv_path}` — Last updated: {time.ctime(mod_time)}")
    st.dataframe(df)
    st.write(df.describe())
else:
    st.warning("CSV file not found. Upload one above.")
