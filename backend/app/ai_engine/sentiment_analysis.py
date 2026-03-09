from textblob import TextBlob

def detect_sentiment(text):

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"

    return "neutral"