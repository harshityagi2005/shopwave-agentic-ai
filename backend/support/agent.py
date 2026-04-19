from .tools import execute_tool


def process_ticket(ticket):

    email = ticket.get("customer_email")
    order_id = ticket.get("order_id")

    # -----------------------------
    # STEP 1: GET CUSTOMER
    # -----------------------------
    customer = execute_tool("get_customer", {
        "email": email
    })

    if not customer.get("found"):
        return {
            "action": "reject",
            "reason": "Customer not found",
            "confidence_score": 0.95,
            "message_to_customer": "We could not verify your account. Please check your email ID."
        }

    # -----------------------------
    # STEP 2: GET ORDER
    # -----------------------------
    order = execute_tool("get_order", {
        "order_id": order_id
    })

    if not order.get("found"):
        return {
            "action": "reject",
            "reason": "Order not found",
            "confidence_score": 0.95,
            "message_to_customer": "We could not find your order in our system."
        }

    # -----------------------------
    # STEP 3: FRAUD DETECTION
    # -----------------------------
    fraud_check = execute_tool("detect_fraud", {
        "customer": customer,
        "order": order
    })

    if fraud_check.get("is_fraud"):
        return {
            "action": "reject",
            "reason": fraud_check.get("reason", "Fraud detected"),
            "confidence_score": 0.98,
            "message_to_customer": "We are unable to process this request after verification."
        }

    # -----------------------------
    # STEP 4: REFUND ELIGIBILITY
    # -----------------------------
    eligibility = execute_tool("check_refund_eligibility", {
        "customer": customer,
        "order": order
    })

    status = eligibility.get("eligible")

    # -----------------------------
    # STEP 5: BUSINESS LOGIC
    # -----------------------------

    # CASE 1: ELIGIBLE REFUND
    if status == True:
        return {
            "action": "refund",
            "reason": "Order eligible under return policy",
            "confidence_score": 0.92,
            "message_to_customer": (
                "Your refund has been approved as per our return policy. "
                "It will be processed within 5–7 business days."
            )
        }

    # CASE 2: NOT ELIGIBLE BUT PREMIUM/VIP FLEXIBILITY
    tier = customer.get("tier", "Standard")

    if tier in ["Premium", "VIP"] and eligibility.get("grace_allowed"):
        return {
            "action": "refund",
            "reason": "Approved under customer tier exception",
            "confidence_score": 0.80,
            "message_to_customer": (
                "As a valued customer, we’ve approved a one-time exception "
                "for your refund request."
            )
        }

    # CASE 3: REPLACEMENT REQUEST (ESCALATE)
    if ticket.get("request_type") == "replacement":
        return {
            "action": "escalate",
            "reason": "Replacement requests require manual review",
            "confidence_score": 0.85,
            "message_to_customer": (
                "Your request has been escalated to our support team for review."
            )
        }

    # CASE 4: DEFAULT REJECT
    return {
        "action": "reject",
        "reason": "Outside return window",
        "confidence_score": 0.90,
        "message_to_customer": (
            "Unfortunately, your request does not meet our return policy criteria."
        )
    }