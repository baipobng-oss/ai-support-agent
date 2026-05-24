memory_store = []

def save_chat(
    customer_id,
    message,
    response
):

    memory_store.append({
        "customer_id": customer_id,
        "message": message,
        "response": response
    })

def get_history(customer_id):

    history = []

    for item in memory_store:

        if item["customer_id"] == customer_id:
            history.append(item)

    return history