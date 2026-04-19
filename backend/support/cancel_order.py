def cancel_order(order_id):
    try:
        order = Order.objects.get(order_id=order_id)

        if order.status != "processing":
            return {
                "success": False,
                "reason": "Order cannot be cancelled (already shipped/delivered)"
            }

        order.status = "cancelled"
        order.save()

        return {
            "success": True,
            "message": "Order cancelled successfully"
        }

    except Order.DoesNotExist:
        return {
            "success": False,
            "reason": "Invalid order ID"
        }