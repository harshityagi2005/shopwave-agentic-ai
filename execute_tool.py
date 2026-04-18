def execute_tool(tool_name, tool_input):
    if tool_name == "get_customer":
        return get_customer(tool_input.get("email"))

    elif tool_name == "get_order":
        return get_order(tool_input.get("order_id"))

    elif tool_name == "check_refund_eligibility":
        return check_refund_eligibility(
            tool_input.get("order_data"),
            tool_input.get("customer_data")
        )

    elif tool_name == "cancel_order":
        return cancel_order(tool_input.get("order_id"))

    elif tool_name == "escalate_ticket":
        return escalate_ticket(
            tool_input.get("reason"),
            tool_input.get("priority", "medium")
        )

    elif tool_name == "search_knowledge_base":
        return search_knowledge_base(tool_input.get("query"))

    else:
        return {"error": f"Unknown tool: {tool_name}"}