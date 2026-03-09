from app.ai_engine.response_generator import generate_response

def generate_review_response(review_text):

    response = generate_response(review_text)

    return response