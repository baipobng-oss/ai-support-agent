from fastapi import APIRouter
import shopify
import os

router = APIRouter(prefix="/shopify")

shop_url = os.getenv("SHOPIFY_STORE")
token = os.getenv("SHOPIFY_ACCESS_TOKEN")

session = shopify.Session(
    shop_url,
    "2024-01",
    token
)

shopify.ShopifyResource.activate_session(
    session
)

@router.get("/order/{order_id}")
def get_order(order_id: str):

    order = shopify.Order.find(order_id)

    return {
        "id": order.id,
        "email": order.email,
        "total": order.total_price,
        "status": order.fulfillment_status
    }