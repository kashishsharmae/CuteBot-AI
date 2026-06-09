import requests

# ==============================
# OFFLINE AI CHAT (OLLAMA)
# ==============================

def chat(question):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": question,
                "stream": False
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json().get("response", "No response")

        return "⚠️ Ollama Error"

    except Exception as e:
        return f"❌ Ollama not running:\n{str(e)}"


# ==============================
# CHECK OLLAMA STATUS
# ==============================

def check_offline_status():
    try:
        requests.get("http://localhost:11434", timeout=3)
        return True
    except:
        return False