def detect_fraud(order_data, customer_data):
    if not order_data.get("found"):
        return True, "Invalid order ID"

    if not customer_data.get("found"):
        return True, "Unknown customer"

    return False, None