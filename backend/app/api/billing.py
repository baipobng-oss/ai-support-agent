from fastapi import APIRouter

from app.services.stripe_service import (
    create_checkout
)

router = APIRouter(prefix="/billing")

@router.get("/checkout")
def checkout():

    url = create_checkout()

    return {
        "checkout_url": url
    }