import requests
import os

# OpenRouter free LLM API key
OPENROUTER_API_KEY = os.getenv(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)
DEEPSEEK_API_KEY = os.getenv(sk-d73af685340e4832bb5cd329dab5f35a)

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
