from dotenv import load_dotenv
import os

load_dotenv()

print("SUPABASE_URL:")
print(os.getenv("SUPABASE_URL"))

print("\nSHOPIFY_STORE:")
print(os.getenv("SHOPIFY_STORE"))

print("\nSLACK_CHANNEL_ID:")
print(os.getenv("SLACK_CHANNEL_ID"))