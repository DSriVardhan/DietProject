import streamlit as st
from openai import OpenAI

st.title("🤖 AI Fitness Assistant")
st.caption("Ask questions about form, diet, or training adjustments.")

openai_api_key = st.secrets.get("OPENAI_API_KEY", None)

if not openai_api_key:
    st.error("Missing OpenAI API Key! Please configure `OPENAI_API_KEY` in Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a professional strength and conditioning coach and sports nutritionist."},
        {"role": "assistant", "content": "Hello! How can I help you reach your goals today?"}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("E.g., How do I increase my bench press safely?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
