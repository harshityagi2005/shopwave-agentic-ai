from .get_customer import get_customer
from .get_order import get_order

def execute_tool(name, input):
    if name == "get_customer":
        return get_customer(input.get("email"))

    elif name == "get_order":
        return get_order(input.get("order_id"))

    return {"error": "tool not found"}