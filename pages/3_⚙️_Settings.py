import streamlit as st

st.title("⚙ Settings")

split = st.slider(
    "Train Size",
    0.5,
    0.9,
    0.8
)

seed = st.number_input(
    "Random Seed",
    0,
    99999,
    42
)

cv = st.slider(
    "Cross Validation Folds",
    2,
    10,
    5
)

st.session_state["split"]=split
st.session_state["seed"]=seed
st.session_state["cv"]=cv

st.success("Settings Saved")
