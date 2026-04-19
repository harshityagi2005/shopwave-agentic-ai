def check_refund_eligibility(order_data, customer_data):
    if not order_data.get("found"):
        return {"eligible": False, "reason": "Invalid order"}

    if not order_data.get("delivery_date"):
        return {"eligible": False, "reason": "Order not delivered yet"}

    delivery_date = datetime.datetime.fromisoformat(order_data["delivery_date"])
    days_since_delivery = (now() - delivery_date).days

    tier = customer_data.get("tier", "Standard")

    max_window = 30  # default

    for item in order_data["items"]:
        category = item["category"].lower()

        if "smart" in category or "laptop" in category:
            max_window = min(max_window, 15)
        elif "accessory" in category or "cable" in category:
            max_window = max(max_window, 60)

    # Tier-based flexibility
    if days_since_delivery <= max_window:
        return {"eligible": True, "reason": "Within return window"}

    if tier == "Premium" and days_since_delivery <= max_window + 3:
        return {"eligible": True, "reason": "Premium grace period"}

    if tier == "VIP":
        return {"eligible": True, "reason": "VIP override (check notes)"}

    return {
        "eligible": False,
        "reason": f"Exceeded return window ({days_since_delivery} days)"
    }