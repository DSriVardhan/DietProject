import streamlit as st

st.title("🏋️‍♂️ Muscle Workout Plans")
st.caption("Select your fitness level and focus area to view recommended workouts.")

# User Selection Controls
col1, col2 = st.columns(2)

with col1:
    level = st.selectbox("Select Experience Level", ["Beginner", "Intermediate", "Advanced"])

with col2:
    muscle_group = st.selectbox("Select Target Muscle Group", ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"])

st.divider()

# Exercise Database mapped to reliable video demonstration links
exercises = {
    "Chest": [
        {
            "name": "Barbell Bench Press", 
            "sets": "3-4", 
            "reps": "8-12", 
            "notes": "Keep feet flat on the floor, retract shoulder blades, and lower the bar to mid-chest.",
            "video": "https://www.youtube.com/watch?v=rT7DgCr-3pg"
        },
        {
            "name": "Incline Dumbbell Press", 
            "sets": "3-4", 
            "reps": "10-12", 
            "notes": "Set bench to 30 degrees to target upper chest without over-engaging shoulders.",
            "video": "https://www.youtube.com/watch?v=8iPEnn-ltC8"
        }
    ],
    "Back": [
        {
            "name": "Lat Pulldowns", 
            "sets": "3-4", 
            "reps": "10-12", 
            "notes": "Pull bar towards upper chest while driving elbows down and squeezing shoulder blades.",
            "video": "https://www.youtube.com/watch?v=CAwf7n6Luuc"
        },
        {
            "name": "Barbell Bent Over Row", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Hinge at hips with a neutral spine and pull barbell toward your lower ribs.",
            "video": "https://www.youtube.com/watch?v=FWJR5Ve8bnQ"
        }
    ],
    "Legs": [
        {
            "name": "Barbell Full Squat", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Keep chest up, brace core, and lower hips down to parallel or lower.",
            "video": "https://www.youtube.com/watch?v=ultWZbUMPL8"
        },
        {
            "name": "Leg Press", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Place feet shoulder-width on platform. Avoid locking out knees at top.",
            "video": "https://www.youtube.com/watch?v=IZxyjW7MPJQ"
        }
    ],
    "Shoulders": [
        {
            "name": "Overhead Military Press", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Keep core tight and press barbell vertically over head without arching lower back.",
            "video": "https://www.youtube.com/watch?v=2yjwXTZQDDI"
        },
        {
            "name": "Dumbbell Lateral Raise", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Raise dumbbells out to sides until parallel with floor while leading with elbows.",
            "video": "https://www.youtube.com/watch?v=3VcKaXpzqRo"
        }
    ],
    "Arms": [
        {
            "name": "Dumbbell Bicep Curl", 
            "sets": "3", 
            "reps": "10-12", 
            "notes": "Keep upper arms stationary and curl weights toward shoulders while squeezing bicep.",
            "video": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"
        },
        {
            "name": "Triceps Cable Pushdown", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Keep elbows tucked to sides and extend arms down completely.",
            "video": "https://www.youtube.com/watch?v=2-LAMcpzODU"
        }
    ],
    "Core": [
        {
            "name": "Abdominal Crunch", 
            "sets": "3", 
            "reps": "15-20", 
            "notes": "Lie flat, contract abs to lift shoulder blades off ground without straining neck.",
            "video": "https://www.youtube.com/watch?v=Xyd_fa5zoEU"
        },
        {
            "name": "Plank", 
            "sets": "3", 
            "reps": "45-60s hold", 
            "notes": "Maintain a straight line from shoulders to ankles with a tight core.",
            "video": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
        }
    ]
}

# Display Exercises
selected_list = exercises.get(muscle_group, [])

st.subheader(f"{level} - {muscle_group} Routine")

for ex in selected_list:
    with st.expander(f"📌 {ex['name']} ({ex['sets']} sets x {ex['reps']})", expanded=True):
        st.write(f"**Execution Notes:** {ex['notes']}")
        
        try:
            st.video(ex["video"])
        except Exception:
            st.info(f"🏋️ Form Guide: Maintain controlled movement during {ex['name']}.")
