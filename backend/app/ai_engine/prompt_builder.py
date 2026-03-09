def build_prompt(review, sentiment):

    prompt = f"""
Customer Review: {review}

Sentiment: {sentiment}

Generate a polite and professional response.
"""

    return prompt