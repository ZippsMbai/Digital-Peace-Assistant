#!/bin/bash
# Start Streamlit in background
streamlit run app.py &

# Start ngrok on Streamlit port 8501
ngrok http 8501

chmod +x start.sh
