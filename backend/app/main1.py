from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.shopify import router as shopify_router
import os
from app.api.auth import router as auth_router

print(os.getenv("SUPABASE_URL"))
print(os.getenv("SHOPIFY_STORE"))

load_dotenv()

app = FastAPI()

app.include_router(chat_router)
app.include_router(shopify_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "AI Support Agent Running"}