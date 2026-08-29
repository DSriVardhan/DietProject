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

# Comprehensive Exercise Database with Anatomical Targeting
exercises = {
    "Chest": [
        {
            "name": "Barbell Bench Press",
            "sets": "3-4",
            "reps": "8-12",
            "target": "Middle Chest (Pectoralis Major - Sternal Head)",
            "synergists": "Triceps Brachii, Anterior Deltoid",
            "notes": "Keep feet flat, retract shoulder blades, and lower the bar to mid-chest with controlled speed."
        },
        {
            "name": "Incline Dumbbell Press",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Upper Chest (Pectoralis Major - Clavicular Head)",
            "synergists": "Anterior Deltoid, Triceps",
            "notes": "Set bench to 30 degrees. Press dumbbells up in a slight arc without touching them at the top."
        },
        {
            "name": "Pec Deck Fly (Machine Fly)",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Inner & Middle Chest (Pectoralis Major Isolation)",
            "synergists": "Anterior Deltoid",
            "notes": "Keep a slight bend in elbows, focus on bringing elbows together, and squeeze at full contraction."
        },
        {
            "name": "Decline Cable Fly",
            "sets": "3",
            "reps": "12-15",
            "target": "Lower Chest (Pectoralis Major - Costal Head)",
            "synergists": "Anterior Deltoid",
            "notes": "Set cables high, pull downwards and together in front of your hips."
        }
    ],
    "Back": [
        {
            "name": "Lat Pulldown",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Upper Lats (Latissimus Dorsi - Width)",
            "synergists": "Teres Major, Biceps Brachii, Brachialis",
            "notes": "Drive elbows straight down toward your ribs while keeping chest lifted."
        },
        {
            "name": "T-Bar Row",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Mid-Back Thickness (Rhomboids & Trapezius)",
            "synergists": "Latissimus Dorsi, Posterior Deltoid",
            "notes": "Hinge at hips, keep lower back neutral, and pull handle toward upper abs."
        },
        {
            "name": "Single-Arm Dumbbell Row",
            "sets": "3",
            "reps": "10-12",
            "target": "Lower Lats & Mid-Back",
            "synergists": "Rhomboids, Rear Delts, Biceps",
            "notes": "Support body on bench, pull dumbbell toward hip rather than straight up to chest."
        },
        {
            "name": "Seated Cable Row",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Mid-Back & Lower Traps",
            "synergists": "Rhomboids, Latissimus Dorsi",
            "notes": "Avoid excessive swinging; squeeze shoulder blades tightly together at full pull."
        }
    ],
    "Legs": [
        {
            "name": "Barbell Squat",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Quadriceps & Gluteus Maximus",
            "synergists": "Adductor Magnus, Soleus, Core",
            "notes": "Brace core, lower hips to parallel or lower, drive upward through mid-foot."
        },
        {
            "name": "Leg Press",
            "sets": "3-4",
            "reps": "10-12",
            "target": "Overall Quadriceps (Rectus Femoris & Vastus Lateralis)",
            "synergists": "Glutes, Hamstrings",
            "notes": "Place feet shoulder-width apart; do not lock out knees at the top."
        },
        {
            "name": "Romanian Deadlift (RDL)",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Hamstrings & Gluteal Fold",
            "synergists": "Erector Spinae, Adductor Magnus",
            "notes": "Hinge at hips pushing butt back, keeping bar close to legs with slight knee bend."
        },
        {
            "name": "Standing Calf Raise",
            "sets": "4",
            "reps": "15-20",
            "target": "Calves (Gastrocnemius)",
            "synergists": "Soleus",
            "notes": "Pause for 1 second at the bottom stretch and squeeze fully on toes."
        }
    ],
    "Shoulders": [
        {
            "name": "Overhead Barbell Press",
            "sets": "3-4",
            "reps": "8-10",
            "target": "Front Shoulders (Anterior Deltoid)",
            "synergists": "Triceps Brachii, Upper Trapezius",
            "notes": "Keep glutes and core tight; press barbell straight up over ears."
        },
        {
            "name": "Dumbbell Lateral Raise",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Side Shoulders (Lateral Deltoid - Width)",
            "synergists": "Supraspinatus, Trapezius",
            "notes": "Lead with elbows and raise weights to shoulder height without swinging body."
        },
        {
            "name": "Reverse Pec Deck (Rear Delt Fly)",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Rear Shoulders (Posterior Deltoid)",
            "synergists": "Rhomboids, Infraspinatus",
            "notes": "Keep hands relaxed and drive handles outward using back of shoulders."
        }
    ],
    "Arms": [
        {
            "name": "Dumbbell Bicep Curl",
            "sets": "3",
            "reps": "10-12",
            "target": "Biceps (Biceps Brachii - Short & Long Heads)",
            "synergists": "Brachialis, Brachioradialis",
            "notes": "Keep elbows fixed to sides; rotate wrist upward as you lift."
        },
        {
            "name": "Hammer Curls",
            "sets": "3",
            "reps": "10-12",
            "target": "Brachialis & Forearms (Brachioradialis)",
            "synergists": "Biceps Brachii",
            "notes": "Hold dumbbells with palms facing each other throughout movement."
        },
        {
            "name": "Triceps Rope Pushdown",
            "sets": "3-4",
            "reps": "12-15",
            "target": "Triceps (Lateral & Medial Heads)",
            "synergists": "Anconeus",
            "notes": "Keep upper arms still; spread rope ends apart at bottom extension."
        },
        {
            "name": "Skull Crushers (EZ-Bar Extension)",
            "sets": "3",
            "reps": "10-12",
            "target": "Triceps (Long Head)",
            "synergists": "Lateral Head",
            "notes": "Lower bar toward forehead/behind head while keeping elbows pointed up."
        }
    ],
    "Core": [
        {
            "name": "Hanging Leg Raise",
            "sets": "3",
            "reps": "12-15",
            "target": "Lower Abs (Rectus Abdominis - Inferior)",
            "synergists": "Hip Flexors, Obliques",
            "notes": "Curl pelvis upward toward chest rather than just swinging legs."
        },
        {
            "name": "Cable Woodchoppers",
            "sets": "3",
            "reps": "12-15",
            "target": "Side Abs (Internal & External Obliques)",
            "synergists": "Transverse Abdominis",
            "notes": "Rotate through torso while keeping arms straight and hip movement stable."
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
