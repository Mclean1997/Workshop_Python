import streamlit as st
from utils.loader import load_data

st.title("📂 Upload Dataset")

uploaded = st.file_uploader(
    "Upload your dataset",
    type=["csv","xlsx","xls","rds","rdata"]
)

if uploaded:

    df = load_data(uploaded)

    st.session_state["df"] = df

    st.success("Dataset Loaded Successfully!")

    st.write(df.head())

    st.write("Rows:",df.shape[0])

    st.write("Columns:",df.shape[1])
