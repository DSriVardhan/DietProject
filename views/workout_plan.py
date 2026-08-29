import streamlit as st

st.title("🏋️‍♂️ Detailed Muscle Workout Plans")

level = st.radio("Select Experience Level:", ["Beginner", "Intermediate", "Advanced"], horizontal=True)
muscle = st.selectbox("Select Muscle Group:", ["Chest", "Back", "Shoulders", "Biceps", "Triceps", "Forearms", "Legs"])

DEMO_VISUAL = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWJnand4cXFwcGNndDRxbHdyNmRycTF2Ym9oZ3c0bzRmc3N5eWZpciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKuXre9U81vThL2/giphy.gif"

workouts = {
    "Chest": {
        "Beginner": [{"name": "Push-ups", "sets": "3", "reps": "8 - 12", "rest": "60s"}, {"name": "Flat Dumbbell Press", "sets": "3", "reps": "10 - 12", "rest": "90s"}],
        "Intermediate": [{"name": "Incline Barbell Bench Press", "sets": "4", "reps": "8 - 10", "rest": "90s"}, {"name": "Cable Flyes", "sets": "3", "reps": "12 - 15", "rest": "60s"}],
        "Advanced": [{"name": "Heavy Barbell Bench Press", "sets": "5", "reps": "3 - 5", "rest": "3 min"}, {"name": "Weighted Chest Dips", "sets": "4", "reps": "6 - 8", "rest": "2 min"}]
    },
    "Back": {
        "Beginner": [{"name": "Lat Pulldowns", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Intermediate": [{"name": "Pull-ups", "sets": "4", "reps": "6 - 10", "rest": "90s"}],
        "Advanced": [{"name": "Deadlifts", "sets": "4", "reps": "4 - 6", "rest": "3 min"}]
    },
    "Shoulders": {
        "Beginner": [{"name": "Dumbbell Press", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Intermediate": [{"name": "Overhead Barbell Press", "sets": "4", "reps": "6 - 8", "rest": "90s"}],
        "Advanced": [{"name": "Push Press", "sets": "4", "reps": "4 - 6", "rest": "2 min"}]
    },
    "Biceps": {
        "Beginner": [{"name": "Dumbbell Curls", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Intermediate": [{"name": "Preacher Curls", "sets": "3", "reps": "8 - 10", "rest": "90s"}],
        "Advanced": [{"name": "EZ-Bar Curls (Drop sets)", "sets": "4", "reps": "8 - 10", "rest": "60s"}]
    },
    "Triceps": {
        "Beginner": [{"name": "Rope Pushdowns", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Intermediate": [{"name": "Skull Crushers", "sets": "3", "reps": "8 - 10", "rest": "90s"}],
        "Advanced": [{"name": "Close-Grip Bench Press", "sets": "4", "reps": "6 - 8", "rest": "2 min"}]
    },
    "Forearms": {
        "Beginner": [{"name": "Wrist Curls", "sets": "3", "reps": "12 - 15", "rest": "45s"}],
        "Intermediate": [{"name": "Reverse Curls", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Advanced": [{"name": "Dead Hangs", "sets": "4", "reps": "Max Time", "rest": "90s"}]
    },
    "Legs": {
        "Beginner": [{"name": "Goblet Squats", "sets": "3", "reps": "10 - 12", "rest": "60s"}],
        "Intermediate": [{"name": "Barbell Squats", "sets": "4", "reps": "8 - 10", "rest": "2 min"}],
        "Advanced": [{"name": "Front Squats", "sets": "4", "reps": "4 - 6", "rest": "3 min"}]
    }
}

selected_routine = workouts.get(muscle, {}).get(level, [])

st.subheader(f"{level} {muscle} Routine")
for idx, ex in enumerate(selected_routine, start=1):
    with st.expander(f"**{idx}. {ex['name']}**", expanded=True):
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.write(f"**Sets:** {ex['sets']}")
            st.write(f"**Reps:** {ex['reps']}")
            st.write(f"**Rest:** {ex['rest']}")
        with col2:
            # Replace the old DEMO_VISUAL line with a working image source:
DEMO_VISUAL = "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80"

try:
    st.image(DEMO_VISUAL, caption=f"Form: {ex['name']}", use_container_width=True)
except Exception:
    st.info(f"🏋️ Form Guide: Keep control and maintain solid posture during {ex['name']}.")
