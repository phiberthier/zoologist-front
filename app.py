import streamlit as st
import requests

st.markdown("""
# What can of penguins are you looking for?""")

island = st.selectbox(
    "What island is your penguin from",
    ["Biscoe", "Dream", "Torgersen"]
)
bill_length = st.number_input('Bill length:', 200.0)
bill_depth = st.number_input('Bill depth:', 200.0)
flipper_depth = st.number_input('Flipper depth:', 400.0)
body_mass = st.number_input('Body mass:', 4000.0)
sex = st.selectbox(
    "Male or Female?",
    ["Male", "Female"]
)

url = "http://localhost:8111/predict"

params = {"island": island,
              "bill_length_mm": bill_length,
              "bill_depth_mm": bill_depth,
              "flipper_length_mm": flipper_depth,
              "body_mass_g": body_mass,
              "sex": sex}

response = requests.get(url=url, params=params).json()["prediction"]

st.markdown(f"# You have a {response} !!!")
