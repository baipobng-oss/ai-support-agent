from openai import OpenAI

client = OpenAI()

def generate_reply(ticket):

    prompt = f"""
    Write a professional support reply.

    Ticket:
    {ticket}
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