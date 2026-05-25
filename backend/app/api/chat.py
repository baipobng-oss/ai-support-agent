from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.support_chain import support_agent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/support/")
def support_chat(req: ChatRequest):

    try:

        response = support_agent(req.message)

        return {
            "response": response
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "error": str(e)
        }