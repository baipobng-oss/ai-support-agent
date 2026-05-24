usage = {}

LIMIT = 500

def check_limit(user_id):

    current = usage.get(user_id, 0)

    if current >= LIMIT:
        return False

    usage[user_id] = current + 1

    return True