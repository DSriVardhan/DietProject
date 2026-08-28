# DietProject
import streamlit as st

st.set_page_config(
    page_title="Calorie & Protein Calculator",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 Calorie & Protein Calculator")
st.caption("Calculate your estimated daily calories and protein needs.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=19, step=1)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=176.0, step=0.5)

with col2:
    weight = st.number_input("Weight (kg)", min_value=25.0, max_value=250.0, value=65.0, step=0.5)
    gender = st.selectbox("Gender", ["Male", "Female"])

activity = st.selectbox(
    "Activity level",
    [
        "Sedentary — little/no exercise",
        "Lightly active — 1–3 days/week",
        "Moderately active — 3–5 days/week",
        "Very active — 6–7 days/week",
        "Extremely active — hard training/physical job",
    ],
)

goal = st.selectbox(
    "Your goal",
    ["Lose weight", "Maintain weight", "Gain weight"]
)

if st.button("Calculate", type="primary", use_container_width=True):
    # Mifflin-St Jeor equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_factors = {
        "Sedentary — little/no exercise": 1.2,
        "Lightly active — 1–3 days/week": 1.375,
        "Moderately active — 3–5 days/week": 1.55,
        "Very active — 6–7 days/week": 1.725,
        "Extremely active — hard training/physical job": 1.9,
    }

    maintenance = bmr * activity_factors[activity]

    if goal == "Lose weight":
        calories = maintenance - 300
        protein_factor = 1.8
    elif goal == "Gain weight":
        calories = maintenance + 300
        protein_factor = 1.8
    else:
        calories = maintenance
        protein_factor = 1.6

    protein = weight * protein_factor

    st.success("Your estimated daily targets:")

    c1, c2 = st.columns(2)
    with c1:
        st.metric("🔥 Calories", f"{calories:,.0f} kcal/day")
    with c2:
        st.metric("💪 Protein", f"{protein:,.0f} g/day")

    st.subheader("Your numbers")
    st.write(f"**Estimated BMR:** {bmr:,.0f} kcal/day")
    st.write(f"**Estimated maintenance calories:** {maintenance:,.0f} kcal/day")

    st.info(
        "These are estimates, not medical advice. Your actual calorie needs can vary "
        "with training, body composition, sleep, and other factors."
    )

st.divider()
st.caption("Built with Python + Streamlit 🐍")