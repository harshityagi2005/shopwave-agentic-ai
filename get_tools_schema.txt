def get_tools_schema():
    return [
        {
            "name": "get_customer",
            "description": "Fetch customer by email",
            "input_schema": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"}
                },
                "required": ["email"]
            }
        },
        ...
    ]