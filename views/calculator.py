import streamlit as st

st.title("🥗 Calorie & Macro Calculator")
st.caption("Determine your daily energy and nutrient targets.")

with st.form("calc_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=10, max_value=100, value=22, step=1)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=175.0, step=0.5)
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        weight = st.number_input("Weight (kg)", min_value=25.0, max_value=250.0, value=70.0, step=0.5)
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
        goal = st.selectbox("Your goal", ["Lose weight", "Maintain weight", "Gain weight"])

    submitted = st.form_submit_button("Calculate Targets", type="primary", use_container_width=True)

if submitted:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
    act_map = {
        "Sedentary — little/no exercise": 1.2,
        "Lightly active — 1–3 days/week": 1.375,
        "Moderately active — 3–5 days/week": 1.55,
        "Very active — 6–7 days/week": 1.725,
        "Extremely active — hard training/physical job": 1.9,
    }
    tdee = bmr * act_map[activity]
    adj = -300 if goal == "Lose weight" else (300 if goal == "Gain weight" else 0)
    target_cal = tdee + adj
    
    protein_g = weight * (1.8 if goal != "Maintain weight" else 1.6)
    fat_g = (target_cal * 0.25) / 9
    carb_g = (target_cal - (protein_g * 4 + fat_g * 9)) / 4

    st.success("Target Calculated!")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Calories", f"{target_cal:,.0f} kcal")
    c2.metric("Protein", f"{protein_g:,.0f} g")
    c3.metric("Fats", f"{fat_g:,.0f} g")
    c4.metric("Carbs", f"{carb_g:,.0f} g")
