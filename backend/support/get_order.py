from .models import Order

def get_order(order_id):
    try:
        order = Order.objects.get(order_id=order_id)

        items = []
        total_amount = 0

        for item in order.items.all():
            product = item.product
            price = float(product.price)
            total_amount += price * item.quantity

            items.append({
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": price,
                "quantity": item.quantity
            })

        return {
            "found": True,
            "order_id": order.order_id,
            "status": order.status,
            "order_date": str(order.order_date),
            "delivery_date": str(order.delivery_date) if order.delivery_date else None,
            "items": items,
            "total_amount": total_amount
        }

    except Order.DoesNotExist:
        return {
            "found": False,
            "error": "Invalid order ID (possible fraud)"
        }