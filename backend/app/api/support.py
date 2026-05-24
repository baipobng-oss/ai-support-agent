from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.support_chain import support_agent
from app.services.ticket_classifier import classify_ticket
from app.services.escalation import needs_human
from app.services.slack_notify import send_to_support

router = APIRouter(prefix="/support")

class SupportRequest(BaseModel):
    message: str

@router.post("/")
async def support(req: SupportRequest):

    category = classify_ticket(
        req.message
    )

    ai_response = support_agent(
        req.message
    )

    escalation = needs_human(
        req.message
    )

    if escalation:

        send_to_support(
            f"ESCALATED TICKET:\n\n{req.message}"
        )

    return {
        "category": category,
        "response": ai_response,
        "escalated": escalation
    }