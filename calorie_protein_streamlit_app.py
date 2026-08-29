# DietProject
import streamlit as st

st.set_page_config(
    page_title="Ultimate Fitness Companion",
    page_icon="🥗",
    layout="wide"
)

# Navigation router across different page views
calculator_page = st.Page("views/calculator.py", title="Calorie & Macro Calculator", icon="🥗", default=True)
workout_page = st.Page("views/workout_plan.py", title="Muscle Workout Plans", icon="🏋️‍♂️")
ai_page = st.Page("views/ai_assistant.py", title="AI Fitness Assistant", icon="🤖")

pg = st.navigation({
    "Tools": [calculator_page, workout_page],
    "AI Support": [ai_page]
})

pg.run()
