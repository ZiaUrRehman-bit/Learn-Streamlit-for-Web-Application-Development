import streamlit as st
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

st.title("Text Analytics")

# Text input
text = st.text_area("Enter text:")

if text:
    # Create a word cloud
    wordcloud = WordCloud().generate(text)
    st.image(wordcloud.to_array())

    # Perform sentiment analysis
    analysis = TextBlob(text)
    st.write("Sentiment Analysis:")
    st.write(f"Polarity: {analysis.sentiment.polarity}")
    st.write(f"Subjectivity: {analysis.sentiment.subjectivity}")
