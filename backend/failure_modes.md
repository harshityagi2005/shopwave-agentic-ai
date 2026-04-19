# ⚠️ Failure Modes – ShopWave AI Agent

This document outlines common failure scenarios in the ShopWave Agentic AI system and how the system handles them gracefully.

The system is designed with a **tool-based agent loop architecture**, so failures are expected and handled at different layers: API layer, tool layer, and data layer.

---

## 🧩 1. Customer Not Found (Data Missing)

### ❌ Scenario
The agent receives a ticket with a valid request, but the customer email does not exist in the database (`customers.json`).

Example input:
```json
{
  "customer_email": "unknown@email.com",
  "order_id": "ORD-001"
}




##   2. FileNotFoundError: customers.json

#   SYSTEM HANDLING
{
  "found": false,
  "error": "customers.json file not found"
}


##   3. {
  "customer_email": ""
}



#  SYSTEM HANDLING
email = ticket.get("customer_email")
if not email:
    return error_response