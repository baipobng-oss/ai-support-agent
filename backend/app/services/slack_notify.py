from slack_sdk import WebClient
import os

client = WebClient(
    token=os.getenv("SLACK_BOT_TOKEN")
)

def send_to_support(message):

    client.chat_postMessage(
        channel=os.getenv("SLACK_CHANNEL_ID"),
        text=message
    )