import plotly.express as px
import pandas as pd

def plot_sentiment_toxicity(df):
    fig = px.scatter(df, x="date", y="sentiment_score", color="toxicity_score",
                     hover_data=['text'], title="Sentiment and Toxicity Over Time")
    return fig
