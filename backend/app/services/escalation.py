NEGATIVE_WORDS = [
    "angry",
    "terrible",
    "refund now",
    "lawsuit",
    "cancel"
]

def needs_human(message):

    text = message.lower()

    for word in NEGATIVE_WORDS:
        if word in text:
            return True

    return False
