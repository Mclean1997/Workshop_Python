import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Exploratory Data Analysis")

if "df" not in st.session_state:

    st.warning("Please upload data first.")

    st.stop()

df = st.session_state["df"]

st.subheader("Dataset")

st.dataframe(df)

st.subheader("Shape")

st.write(df.shape)

st.subheader("Columns")

st.write(df.columns.tolist())

st.subheader("Missing Values")

st.dataframe(df.isnull().sum())

st.subheader("Duplicates")

st.write(df.duplicated().sum())

st.subheader("Data Types")

st.dataframe(df.dtypes)

st.subheader("Statistics")

st.dataframe(df.describe(include="all"))

numeric = df.select_dtypes("number").columns

if len(numeric)>0:

    variable = st.selectbox(
        "Histogram",
        numeric
    )

    fig = px.histogram(
        df,
        x=variable
    )

    st.plotly_chart(fig,use_container_width=True)

if len(numeric)>1:

    corr = df[numeric].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto"
    )

    st.plotly_chart(fig,use_container_width=True)

st.subheader("Target Variable")

target = st.selectbox(
    "Choose Target",
    ["None"]+list(df.columns)
)

if target!="None":

    st.session_state["target"]=target

    if pd.api.types.is_numeric_dtype(df[target]):

        st.success("Regression Problem Detected")

    else:

        st.success("Classification Problem Detected")
