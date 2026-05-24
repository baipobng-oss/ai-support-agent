import stripe

stripe.api_key = "sk_test_51TUdJVF33aR3QzL4dho1KeephC4Z7wXPRNT0u2iKrOTDdfGH7ocXwwaI3MrAEFaPO7Y2SYJDTaHGDtbh844JWTyP00OrUKPa9G"

def create_checkout():

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],

        line_items=[
            {
                "price": "price_xxxxx",
                "quantity": 1
            }
        ],

        mode="subscription",

        success_url=
        "http://localhost:5173/success",

        cancel_url=
        "http://localhost:5173/cancel"
    )

    return session.url