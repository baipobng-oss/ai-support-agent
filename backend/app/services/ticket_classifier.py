from openai import OpenAI

client = OpenAI()

def classify_ticket(message):

    prompt = f"""
    Classify support ticket:

    Categories:
    - refund
    - shipping
    - technical
    - complaint
    - billing

    Message:
    {message}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content