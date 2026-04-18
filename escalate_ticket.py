def escalate_ticket(reason, priority="medium"):
    return {
        "escalated": True,
        "priority": priority,
        "reason": reason,
        "message": "Ticket escalated to human support"
    }