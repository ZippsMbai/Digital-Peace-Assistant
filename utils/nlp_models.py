from transformers import pipeline

# Sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Toxicity detection
toxicity_pipeline = pipeline("text-classification", model="unitary/toxic-bert")

# Translation EN <-> SW
translation_en_sw = pipeline("translation_en_to_sw", model="Helsinki-NLP/opus-mt-en-sw")
translation_sw_en = pipeline("translation_sw_to_en", model="Helsinki-NLP/opus-mt-sw-en")

def analyze_sentiment(text):
    return sentiment_pipeline(text)[0]

def analyze_toxicity(text):
    return toxicity_pipeline(text)[0]

def translate_to_sw(text):
    return translation_en_sw(text)[0]['translation_text']

def translate_to_en(text):
    return translation_sw_en(text)[0]['translation_text']
