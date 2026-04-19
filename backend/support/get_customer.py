
import json
from pathlib import Path

def get_customer(email):
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "customers.json"

    if not file_path.exists():
        return {
            "found": False,
            "error": "customers.json file not found"
        }

    with open(file_path, "r", encoding="utf-8") as f:
        customers = json.load(f)

    for customer in customers:
        if customer.get("email") == email:
            return {
                "found": True,
                "customer": customer
            }

    return {
        "found": False,
        "message": "Customer not found"
    }