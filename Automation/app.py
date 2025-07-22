# app.py

import streamlit as st
import os
from logic import organize_directory

st.set_page_config(page_title="📂 File Organizer", layout="centered")

# ---------- STYLES ----------
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .stTextInput > label, .stFileUploader > label {
            font-weight: 600;
        }
        .stButton > button {
            background-color: #6c63ff;
            color: white;
            border-radius: 8px;
            height: 3em;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #5a54d1;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("## 📁 File Organizer")
st.markdown("Organize your messy folders into **neat categories** with a single click!")

st.divider()

# ---------- FILE UPLOAD ----------
uploaded_files = st.file_uploader("📤 Upload files to organize:", accept_multiple_files=True, type=None, help="Limit 200MB per file")

# ---------- INPUT PATH ----------
directory_path = st.text_input("📁 Enter absolute folder path where files will be saved and organized:")

# ---------- ORGANIZE BUTTON ----------
if st.button("🚀 Organize Files"):
    if not directory_path.strip():
        st.warning("⚠️ Please enter a valid folder path before organizing.")
    elif not os.path.exists(directory_path):
        st.error("🚫 The specified path does not exist.")
    elif not uploaded_files:
        st.warning("📂 Please upload at least one file to organize.")
    else:
        # Save uploaded files to specified directory
        for file in uploaded_files:
            save_path = os.path.join(directory_path, file.name)
            with open(save_path, "wb") as f:
                f.write(file.read())

        # Organize the directory
        logs = organize_directory(directory_path)
        st.success("✅ Files organized successfully!")
        with st.expander("📜 View Logs"):
            st.text_area("Logs", "\n".join(logs), height=250)

# ---------- FOOTER ----------
st.divider()
st.markdown(
    "<small>Made with  by Krishna | Powered by Python & Streamlit</small>",
    unsafe_allow_html=True
)
