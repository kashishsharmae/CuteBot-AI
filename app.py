import streamlit as st
from chatbot import chat, check_offline_status

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="CuteBot AI 💖",
    page_icon="💬",
    layout="centered"
)

# =========================
# MAGENTA CUTE UI
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff4ecd, #8a2be2);
}

.stApp {
    background: linear-gradient(135deg, #ff4ecd, #8a2be2);
}

h1 {
    color: white;
    text-align: center;
}

.user {
    background: #ffb6f0;
    padding: 10px;
    border-radius: 12px;
    margin: 5px;
}

.bot {
    background: white;
    padding: 10px;
    border-radius: 12px;
    margin: 5px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("💖 CuteBot AI 💬")
st.caption("Cute • Offline • Private AI Assistant 💖")

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# INPUT
# =========================
user_input = st.chat_input("Say something cute 💬")

# =========================
# CHAT LOGIC
# =========================
if user_input:
    st.session_state.messages.append(("user", user_input))
    reply = chat(user_input)
    st.session_state.messages.append(("bot", reply))

# =========================
# TOGGLE HISTORY
# =========================
hide = st.toggle("🙈 Hide Chat History")

# =========================
# DISPLAY CHAT
# =========================
if not hide:
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"<div class='user'>🧑‍💻 {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot'>🤖 {msg}</div>", unsafe_allow_html=True)
else:
    st.info("Chat history hidden 🙈")

# =========================
# STATUS
# =========================
st.sidebar.title("💖 CuteBot AI")

if check_offline_status():
    st.sidebar.success("Ollama Running ✅")
else:
    st.sidebar.error("Ollama Not Running ❌")