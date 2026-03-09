from textblob import TextBlob


def analyze_sentiment(text: str):

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"