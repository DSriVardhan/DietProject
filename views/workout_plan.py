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

# Comprehensive Exercise Database mapped directly to raw GitHub media links
BASE_IMG_URL = "https://raw.githubusercontent.com/yuhas/free-exercise-db/main/exercises"

exercises = {
    "Chest": [
        {
            "name": "Barbell Bench Press", 
            "sets": "3-4", 
            "reps": "8-12", 
            "notes": "Keep feet flat on the floor, retract shoulder blades, and lower the bar to mid-chest.",
            "image": f"{BASE_IMG_URL}/Barbell_Bench_Press/0.jpg"
        },
        {
            "name": "Incline Dumbbell Press", 
            "sets": "3-4", 
            "reps": "10-12", 
            "notes": "Set bench to 30 degrees to target upper chest without over-engaging shoulders.",
            "image": f"{BASE_IMG_URL}/Incline_Dumbbell_Press/0.jpg"
        }
    ],
    "Back": [
        {
            "name": "Lat Pulldowns", 
            "sets": "3-4", 
            "reps": "10-12", 
            "notes": "Pull bar towards upper chest while driving elbows down and squeezing shoulder blades.",
            "image": f"{BASE_IMG_URL}/Cable_Pulldown/0.jpg"
        },
        {
            "name": "Barbell Bent Over Row", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Hinge at hips with a neutral spine and pull barbell toward your lower ribs.",
            "image": f"{BASE_IMG_URL}/Barbell_Bent_Over_Row/0.jpg"
        }
    ],
    "Legs": [
        {
            "name": "Barbell Full Squat", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Keep chest up, brace core, and lower hips down to parallel or lower.",
            "image": f"{BASE_IMG_URL}/Barbell_Full_Squat/0.jpg"
        },
        {
            "name": "Leg Press", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Place feet shoulder-width on platform. Avoid locking out knees at top.",
            "image": f"{BASE_IMG_URL}/Sled_45_Degree_Leg_Press/0.jpg"
        }
    ],
    "Shoulders": [
        {
            "name": "Overhead Military Press", 
            "sets": "3-4", 
            "reps": "8-10", 
            "notes": "Keep core tight and press barbell vertically over head without arching lower back.",
            "image": f"{BASE_IMG_URL}/Barbell_Standing_Military_Press/0.jpg"
        },
        {
            "name": "Dumbbell Lateral Raise", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Raise dumbbells out to sides until parallel with floor while leading with elbows.",
            "image": f"{BASE_IMG_URL}/Dumbbell_Lateral_Raise/0.jpg"
        }
    ],
    "Arms": [
        {
            "name": "Dumbbell Bicep Curl", 
            "sets": "3", 
            "reps": "10-12", 
            "notes": "Keep upper arms stationary and curl weights toward shoulders while squeezing bicep.",
            "image": f"{BASE_IMG_URL}/Dumbbell_Bicep_Curl/0.jpg"
        },
        {
            "name": "Triceps Cable Pushdown", 
            "sets": "3", 
            "reps": "12-15", 
            "notes": "Keep elbows tucked to sides and extend arms down completely.",
            "image": f"{BASE_IMG_URL}/Triceps_Pushdown/0.jpg"
        }
    ],
    "Core": [
        {
            "name": "Abdominal Crunch", 
            "sets": "3", 
            "reps": "15-20", 
            "notes": "Lie flat, contract abs to lift shoulder blades off ground without straining neck.",
            "image": f"{BASE_IMG_URL}/Ab_Crunch_Machine/0.jpg"
        },
        {
            "name": "Ab Roller Rollout", 
            "sets": "3", 
            "reps": "10-12", 
            "notes": "Kneel down, hold roller, extend forward maintaining flat spine, pull back with abs.",
            "image": f"{BASE_IMG_URL}/Ab_Roller/0.jpg"
        }
    ]
}

# Display Exercises
selected_list = exercises.get(muscle_group, [])

st.subheader(f"{level} - {muscle_group} Routine")

for ex in selected_list:
    with st.expander(f"📌 {ex['name']} ({ex['sets']} sets x {ex['reps']} reps)", expanded=True):
        st.write(f"**Execution Notes:** {ex['notes']}")
        
        try:
            st.image(ex["image"], caption=f"Form Guide: {ex['name']}", use_container_width=True)
        except Exception:
            st.info(f"🏋️ Form Guide: Maintain controlled movement during {ex['name']}.")
