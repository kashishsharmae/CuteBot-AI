import streamlit as st
from chatbot import online_chat, offline_chat, check_offline_status

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="FlexiMode AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
}

.sub-title {
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.status-box {
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">🤖 FlexiMode AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Online Gemini + Offline Ollama AI Assistant</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.header("⚙️ Settings")

    mode = st.radio(
        "Select AI Mode",
        ["Online (Gemini)", "Offline (Ollama)"]
    )

    st.divider()

    st.subheader("System Status")

    if check_offline_status():
        st.success("🟢 Ollama Connected")
    else:
        st.error("🔴 Ollama Not Running")

# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# USER INPUT
# =========================

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            if mode == "Online (Gemini)":
                response = online_chat(prompt)

            else:
                response = offline_chat(prompt)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "Developed by Kashish Sharma | FlexiMode AI Chatbot"
)
