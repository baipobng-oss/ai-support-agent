from fastapi import APIRouter

router = APIRouter(prefix="/analytics")

@router.get("/")
def analytics():

    return {

        "tickets_today": 152,

        "ai_resolved": 124,

        "human_escalations": 28,

        "avg_response_time": "12 sec"
    }