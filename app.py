import streamlit as st

st.set_page_config(
    page_title="🧠 Universal ML Studio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 Universal Machine Learning Studio")

st.markdown("""
Welcome to the Universal Machine Learning Studio.

This application automatically adapts to almost any dataset.

### Features

- 📂 Upload CSV, Excel and R files
- 📊 Automatic EDA
- 🧹 Data Cleaning
- 🤖 Machine Learning
- 📈 Model Evaluation
- 🌳 Explainability
- ⬇ Download Results

Use the navigation menu on the left to begin.
""")
