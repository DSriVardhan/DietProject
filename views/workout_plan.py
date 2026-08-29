import streamlit as st

st.title("🏋️‍♂️ Muscle Workout Plans")
st.caption("Select your fitness level and focus area to view targeted exercises and primary muscle activations.")

# Selection Controls
col1, col2 = st.columns(2)

with col1:
    level = st.selectbox("Select Experience Level", ["Beginner", "Intermediate", "Advanced"])

with col2:
    muscle_group = st.selectbox("Select Target Muscle Group", ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"])

st.divider()

# Base link for open-source exercise images
IMG_BASE = "https://images.pexels.com/photos"

# Comprehensive Exercise Database with Anatomical Targeting & Visuals
exercises = {
    "Chest": [
        {
            "name": "Barbell Bench Press",
            "sets": "3-4",
            "reps": "8-12",
            "target": "Middle Chest (Pectoralis Major - Sternal Head)",
            "synergists": "Triceps Brachii, Anterior Deltoid",
            "notes": "Keep feet flat, retract shoulder blades, and lower the bar to mid-chest with controlled speed.",
            "image": "https://images.pexels.com/photos/3837781/pexels-photo-3837781.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Incline Dumbbell Press",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Upper Chest (Pectoralis Major - Clavicular Head)",
            "synergists": "Anterior Deltoid, Triceps",
            "notes": "Set bench to 30 degrees. Press dumbbells up in a slight arc without touching them at the top.",
            "image": "https://images.pexels.com/photos/3838389/pexels-photo-3838389.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Pec Deck Fly (Machine Fly)",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Inner & Middle Chest (Pectoralis Major Isolation)",
            "synergists": "Anterior Deltoid",
            "notes": "Keep a slight bend in elbows, focus on bringing elbows together, and squeeze at full contraction.",
            "image": "https://images.pexels.com/photos/1552242/pexels-photo-1552242.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ],
    "Back": [
        {
            "name": "Lat Pulldown",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Upper Lats (Latissimus Dorsi - Width)",
            "synergists": "Teres Major, Biceps Brachii, Brachialis",
            "notes": "Drive elbows straight down toward your ribs while keeping chest lifted.",
            "image": "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Seated Cable Row",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Mid-Back & Lower Traps",
            "synergists": "Rhomboids, Latissimus Dorsi",
            "notes": "Avoid excessive swinging; squeeze shoulder blades tightly together at full pull.",
            "image": "https://images.pexels.com/photos/3838237/pexels-photo-3838237.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ],
    "Legs": [
        {
            "name": "Barbell Squat",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Quadriceps & Gluteus Maximus",
            "synergists": "Adductor Magnus, Soleus, Core",
            "notes": "Brace core, lower hips to parallel or lower, drive upward through mid-foot.",
            "image": "https://images.pexels.com/photos/4753928/pexels-photo-4753928.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Leg Press",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Overall Quadriceps (Rectus Femoris & Vastus Lateralis)",
            "synergists": "Glutes, Hamstrings",
            "notes": "Place feet shoulder-width apart; do not lock out knees at the top.",
            "image": "https://images.pexels.com/photos/1954524/pexels-photo-1954524.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ],
    "Shoulders": [
        {
            "name": "Overhead Barbell Press",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Front Shoulders (Anterior Deltoid)",
            "synergists": "Triceps Brachii, Upper Trapezius",
            "notes": "Keep glutes and core tight; press barbell straight up over ears.",
            "image": "https://images.pexels.com/photos/1552252/pexels-photo-1552252.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Dumbbell Lateral Raise",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Side Shoulders (Lateral Deltoid - Width)",
            "synergists": "Supraspinatus, Trapezius",
            "notes": "Lead with elbows and raise weights to shoulder height without swinging body.",
            "image": "https://images.pexels.com/photos/3837752/pexels-photo-3837752.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ],
    "Arms": [
        {
            "name": "Dumbbell Bicep Curl",
            "sets": "3",
            "reps": "10-12",
            "target": "Biceps (Biceps Brachii - Short & Long Heads)",
            "synergists": "Brachialis, Brachioradialis",
            "notes": "Keep elbows fixed to sides; rotate wrist upward as you lift.",
            "image": "https://images.pexels.com/photos/4164761/pexels-photo-4164761.jpeg?auto=compress&cs=tinysrgb&w=800"
        },
        {
            "name": "Triceps Cable Pushdown",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Triceps (Lateral & Medial Heads)",
            "synergists": "Anconeus",
            "notes": "Keep upper arms still; spread rope ends apart at bottom extension.",
            "image": "https://images.pexels.com/photos/3837781/pexels-photo-3837781.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ],
    "Core": [
        {
            "name": "Plank Hold",
            "sets": "3",
            "reps": "45-60s hold",
            "target": "Transverse Abdominis & Rectus Abdominis",
            "synergists": "Obliques, Lower Back",
            "notes": "Maintain a flat spine, brace core, and avoid letting hips sag.",
            "image": "https://images.pexels.com/photos/3775566/pexels-photo-3775566.jpeg?auto=compress&cs=tinysrgb&w=800"
        }
    ]
}

# Render Selected Routine
selected_list = exercises.get(muscle_group, [])

st.subheader(f"{level} Level — {muscle_group} Focus Routine")

for ex in selected_list:
    with st.expander(f"📌 {ex['name']} ({ex['sets']} sets x {ex['reps']} reps)", expanded=True):
        st.markdown(f"🎯 **Primary Target:** `{ex['target']}`")
        st.markdown(f"🦾 **Assisting Muscles:** {ex['synergists']}")
        st.markdown(f"💡 **Execution & Form:** {ex['notes']}")
        
        # Display image visually
        try:
            st.image(ex["image"], caption=f"Form Guide: {ex['name']}", use_container_width=True)
        except Exception:
            st.info(f"🏋️ Form Guide: Keep control and maintain solid posture during {ex['name']}.")
