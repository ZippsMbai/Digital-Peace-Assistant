# Digital-Peace-Assistant
LLM Project to help in early detection and mitigation of inflammatory narratives spreading on social meida platforms.  Tool that can analyze online messages that have the potential to escalate local tensions.
# ILRI Digital Peace Assistant

## Features
- Sentiment & toxicity analysis (English + Kiswahili)
- Trend visualization dashboard
- Chatbot powered by OpenRouter + DeepSeek
- ILRI branding
- Deployable via Streamlit Cloud or Ngrok

## Deployment

### Streamlit Cloud
1. Fork repo
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Connect GitHub repo
4. Click **Deploy**

### Ngrok
```bash
pip install pyngrok streamlit
streamlit run app.py &
ngrok http 8501

Environment Variables

OPENROUTER_API_KEY — OpenRouter API key

DEEPSEEK_API_KEY — DeepSeek API key (optional)


---

# ✅ Next Steps

1. Copy all files into a GitHub repository.  
2. Upload `assets/ilri_logo.png` (use official ILRI logo).  
3. Set your **environment variables** for OpenRouter and DeepSeek (optional fallback).  
4. Deploy on **Streamlit Cloud** or run locally via **ngrok**.  
5. Share the live link with investors and teammates.  

---
