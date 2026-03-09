def extract_topics(text):

    keywords = {
        "service": ["service", "staff", "waiter"],
        "delivery": ["delivery", "late"],
        "food": ["food", "taste", "dish"]
    }

    topics = []

    for topic, words in keywords.items():
        for word in words:
            if word in text.lower():
                topics.append(topic)

    return topics