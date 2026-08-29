import streamlit as st

st.title("🏋️‍♂️ Muscle Workout Plans")
st.caption("Select your fitness level and focus area to view recommended workouts.")

# User Selection Controls
col1, col2 = st.columns(2)

with col1:
    level = st.selectbox("Select Experience Level", ["Beginner", "Intermediate", "Advanced"])

with col2:
    muscle_group = st.selectbox("Select Target Muscle Group", ["Chest", "Back", "Legs", "Shoulders", "Arms"])

st.divider()

# Sample Exercise Data
exercises = {
    "Chest": [
        {"name": "Bench Press", "sets": "3-4", "reps": "8-12", "notes": "Keep feet flat on the floor and maintain a controlled motion."},
        {"name": "Incline Dumbbell Press", "sets": "3", "reps": "10-12", "notes": "Set bench to 30 degrees to target upper chest."}
    ],
    "Back": [
        {"name": "Lat Pulldowns", "sets": "3-4", "reps": "10-12", "notes": "Pull bar towards upper chest while squeezing shoulder blades."},
        {"name": "Barbell Rows", "sets": "3", "reps": "8-10", "notes": "Hinge at hips with a flat back."}
    ],
    "Legs": [
        {"name": "Barbell Squats", "sets": "3-4", "reps": "8-10", "notes": "Keep chest up and squat to parallel or lower."},
        {"name": "Leg Press", "sets": "3", "reps": "12-15", "notes": "Avoid locking out your knees at the top."}
    ],
    "Shoulders": [
        {"name": "Overhead Press", "sets": "3-4", "reps": "8-10", "notes": "Core tight, press barbell straight overhead."},
        {"name": "Lateral Raises", "sets": "3", "reps": "12-15", "notes": "Lead with elbows and avoid swinging."}
    ],
    "Arms": [
        {"name": "Bicep Curls", "sets": "3", "reps": "10-12", "notes": "Keep elbows tucked to sides throughout movement."},
        {"name": "Tricep Pushdowns", "sets": "3", "reps": "12-15", "notes": "Keep upper arms stationary."}
    ]
}

# Display Exercises
selected_list = exercises.get(muscle_group, [])

st.subheader(f"{level} - {muscle_group} Routine")

for ex in selected_list:
    with st.expander(f"📌 {ex['name']} ({ex['sets']} sets x {ex['reps']} reps)", expanded=True):
        st.write(f"**Execution Notes:** {ex['notes']}")
        
        # Working image demo URL with fallback handling
        demo_visual = "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=800&q=80"
        
        try:
            st.image(demo_visual, caption=f"Form: {ex['name']}", use_container_width=True)
        except Exception:
            st.info(f"🏋️ Form Guide: Keep control and maintain solid posture during {ex['name']}.")
