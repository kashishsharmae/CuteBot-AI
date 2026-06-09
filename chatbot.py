from google import genai
import requests
import os
import time

# ==================================
# GEMINI ONLINE AI CONFIGURATION
# ==================================

API_KEY = os.getenv("GEMINI_API_KEY")

client = None

if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print("Gemini Initialization Error:", e)

# ==================================
# OFFLINE MODE (OLLAMA + GEMMA)
# ==================================

def offline_chat(question):

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

            data = response.json()

            return data.get(
                "response",
                "No response received from Offline AI."
            )

        return f"""
❌ Offline AI Error

Status Code: {response.status_code}
"""

    except Exception as e:

        return f"""
⚠️ Offline AI Not Available

Reason:
{str(e)}

Possible Fixes:
• Install Ollama
• Run: ollama serve
• Ensure model exists: gemma3:1b
"""

# ==================================
# ONLINE MODE (GEMINI)
# ==================================

def online_chat(question):

    if client is None:
        return """
❌ Gemini API Key Not Found

Set GEMINI_API_KEY environment variable.
"""

    models_to_try = [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
    ]

    for model_name in models_to_try:

        try:

            response = client.models.generate_content(
                model=model_name,
                contents=question
            )

            if hasattr(response, "text"):
                return response.text

            return str(response)

        except Exception as e:

            print(f"Gemini Error ({model_name}): {e}")

            time.sleep(1)

    return f"""
⚠️ Gemini currently unavailable.

Automatically switching to Offline AI...

{offline_chat(question)}
"""

# ==================================
# OLLAMA STATUS CHECK
# ==================================

def check_offline_status():

    try:

        requests.get(
            "http://localhost:11434",
            timeout=3
        )

        return True

    except:

        return False
