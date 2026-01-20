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

    # Interpretation
    if output < 40:
        level = "LOW"
        color = "🟢"
    elif output < 70:
        level = "MEDIUM"
        color = "🟡"
    else:
        level = "HIGH"
        color = "🔴"

    st.subheader("Result")
    st.metric("Irrigation Value", f"{output:.2f}")
    st.success(f"{color} Recommended Irrigation Level: **{level}**")
