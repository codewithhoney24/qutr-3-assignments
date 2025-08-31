from my_guardrails import function_tool

# Simulated order DB
orders = {
    "101": "Shipped",
    "102": "Processing",
    "103": "Delivered"
}

@function_tool
def get_order_status(order_id: str):
    """
    Simulated tool for fetching order status.
    """
    if order_id in orders:
        return {"order_id": order_id, "status": orders[order_id]}
    else:
        return {"error": "Order ID not found"}
