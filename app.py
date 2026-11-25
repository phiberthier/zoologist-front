import streamlit as st
import requests

st.markdown("""
# What kind of penguins are you looking for?""")

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:

    st.header("Penguin characteristics")

    island = st.selectbox(
        "Island",
        ["Biscoe", "Dream", "Torgersen"]
    )

    bill_length = st.slider(
        "Bill length (mm)",
        30.0,
        150.0,
        50.0
    )

    bill_depth = st.slider(
        "Bill depth (mm)",
        10.0,
        40.0,
        18.0
    )

    flipper_length = st.slider(
        "Flipper length (mm)",
        150.0,
        300.0,
        200.0
    )

    body_mass = st.slider(
        "Body mass (g)",
        2500.0,
        7000.0,
        4000.0
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

# island = st.selectbox(
#     "What island is your penguin from",
#     ["Biscoe", "Dream", "Torgersen"]
# )
# bill_length = st.number_input('Bill length:', 50.0)
# bill_depth = st.number_input('Bill depth:', 50.0)
# flipper_depth = st.number_input('Flipper depth:', 50.0)
# body_mass = st.number_input('Body mass:', 4000.0)
# sex = st.selectbox(
#     "Male or Female?",
#     ["Male", "Female"]
# )

### CREATE DYNAMIC ROBOT PORTRAIT
body_radius = body_mass / 80
beak_length = bill_length * 2
beak_height = bill_depth * 0.8
flipper_size = flipper_length / 6

with col2:

    st.header("Robot portrait of your Penguin")

    penguin_svg = f"""
    <svg width="500" height="500">

        <!-- body -->
        <ellipse
            cx="250"
            cy="280"
            rx="{body_radius*1.5}"
            ry="{body_radius*1.5}"
            fill="black"
        />

        <!-- belly -->
        <ellipse
            cx="250"
            cy="300"
            rx="{body_radius*1.5}"
            ry="{body_radius*1.5}"
            fill="white"
        />

        <!-- head -->
        <circle
            cx="250"
            cy="150"
            r="{body_radius*1}"
            fill="black"
        />

        <!-- beak -->
        <polygon
        points="
        {250+body_radius*0.4},{150-beak_height/2}
        {250+body_radius*0.4},{150+beak_height/2}
        {250+body_radius*0.4+beak_length},150"
        fill="orange"
        />



        <!-- left flipper -->
        <ellipse
            cx="{250-body_radius*1.5}"
            cy="280"
            rx="{flipper_size}"
            ry="20"
            fill="black"
            transform="rotate(-25 {250-body_radius*1.5} 280)"
        />

        <!-- right flipper -->
        <ellipse
            cx="{250+body_radius*1.5}"
            cy="280"
            rx="{flipper_size}"
            ry="20"
            fill="black"
            transform="rotate(25 {250+body_radius*1.5} 280)"
        />

    </svg>
    """
with col2:
    st.components.v1.html(
    penguin_svg,
    height=400
    )
    st.markdown("### Is this the one?")
    validate = st.button(
        "Yes",
        type="primary"
    )


### GIVE CORRESPONDING PHOTO

url = st.secrets["API_URL"] + "/predict"

params = {"island": island,
              "bill_length_mm": bill_length,
              "bill_depth_mm": bill_depth,
              "flipper_length_mm": flipper_length,
              "body_mass_g": body_mass,
              "sex": sex}

def predict(params):
    response = requests.get(url=url, params=params)
    return response.json()["prediction"]

prediction = predict(params)


if validate:
    with col3:
        st.markdown(f"# You have a {prediction} !!!")
        if prediction=="Adelie":
            st.image("images/adelie.jpg")
        elif prediction=="Gentoo":
            st.image("images/gentoo.jpg")
        else:
            st.image("images/chinstrap.jpg")
