def route_ticket(category):

    if category == "refund":
        return "billing-team"

    if category == "technical":
        return "engineering"

    if category == "shipping":
        return "logistics"

    return "general-support"