def apply_tone(response, tone="professional"):

    if tone == "friendly":
        return "😊 " + response

    if tone == "formal":
        return "Dear Customer, " + response

    return response