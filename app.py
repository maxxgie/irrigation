import streamlit as st
from fuzzy_logic import build_fuzzy_system

st.set_page_config(page_title="Smart Irrigation System", layout="centered")

st.title("💧 Smart Irrigation Recommendation System")
st.write("Fuzzy Logic–based irrigation control")

# -------- Inputs --------
soil = st.slider("Soil Moisture (%)", 0, 100, 50)
temp = st.slider("Temperature (°C)", 0, 40, 25)
hum = st.slider("Humidity (%)", 0, 100, 50)

if st.button("Compute Irrigation"):
    sim = build_fuzzy_system()

    sim.input['soil_moisture'] = soil
    sim.input['temperature'] = temp
    sim.input['humidity'] = hum

    sim.compute()
    output = sim.output['irrigation']

    if output < 40:
        level = "LOW"
    elif output < 70:
        level = "MEDIUM"
    else:
        level = "HIGH"

    st.success(f"Irrigation Level: **{level}**")
    st.write("Numeric Value:", round(output, 2))
