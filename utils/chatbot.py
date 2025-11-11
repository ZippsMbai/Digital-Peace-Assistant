import requests
import os

# OpenRouter free LLM API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def query_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
    data = {
        "model": "mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        r = requests.post(url, json=data, headers=headers)
        return r.json()["choices"][0]["message"]["content"]
    except:
        return None

def query_deepseek(prompt):
    url = "https://api.deepseek.com/chat"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    data = {"input": prompt}
    try:
        r = requests.post(url, json=data, headers=headers)
        return r.json().get("response")
    except:
        return None

def ask_chatbot(prompt):
    # Try OpenRouter first
    response = query_openrouter(prompt)
    if not response:
        response = query_deepseek(prompt)
    return response or "Sorry, I cannot answer right now."
