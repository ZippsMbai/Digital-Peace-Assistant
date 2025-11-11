import streamlit as st
import pandas as pd
from utils import nlp_models, chatbot, visualizer
from PIL import Image

st.set_page_config(page_title="ILRI Digital Peace Assistant", layout="wide")

# Sidebar branding
logo = Image.open("assets/ilri_logo.png")
st.sidebar.image(logo, width=150)
st.sidebar.markdown("### ILRI Digital Peace Assistant")
st.sidebar.markdown("Monitor community narratives and livestock-related trends")

# File upload
uploaded_file = st.file_uploader("Upload CSV of narratives", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("sample_data/sample_narratives.csv")

# NLP Analysis
df['sentiment'] = df['text'].apply(lambda x: nlp_models.analyze_sentiment(x)['label'])
df['sentiment_score'] = df['text'].apply(lambda x: nlp_models.analyze_sentiment(x)['score'])
df['toxicity'] = df['text'].apply(lambda x: nlp_models.analyze_toxicity(x)['label'])
df['toxicity_score'] = df['text'].apply(lambda x: nlp_models.analyze_toxicity(x)['score'])

# Display table
st.dataframe(df)

# Plot trends
fig = visualizer.plot_sentiment_toxicity(df)
st.plotly_chart(fig, use_container_width=True)

# Chatbot
st.markdown("## Chatbot")
user_input = st.text_area("Ask a question about narratives:")
if st.button("Ask"):
    if user_input:
        answer = chatbot.ask_chatbot(user_input)
        st.markdown(f"**Answer:** {answer}")
