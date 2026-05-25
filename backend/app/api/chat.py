from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.support_chain import support_agent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/support/")
def support_chat(req: ChatRequest):

    response = support_agent(
        req.message
    )

    return {
        "response": response
    }