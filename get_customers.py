def get_customer(email):
    try:
        customer = Customer.objects.get(email=email)
        return {
            "found": True,
            "email": customer.email,
            "name": customer.name,
            "tier": customer.tier,
            "notes": customer.notes
        }
    except Customer.DoesNotExist:
        return {
            "found": False,
            "error": "Customer not found"
        }